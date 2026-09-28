#!/usr/bin/env python3
"""Apply one Agentic Marketplace Listings lifecycle update in a single call.

Resolves the listing, checks the transition, writes the tracked properties,
and moves the item folder. Prints one JSON object. Standard library only.

Exit codes:
  0  applied, or already current (no change)
  2  listing not found or ambiguous (see "candidates")
  3  needs seller approval (correction, reopening, or unusual transition)
  4  missing required values (see "missing")
  5  workspace problem or occupied target folder
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

STAGES = ["1 - Building", "2 - Ready", "3 - Posted", "4 - Sold", "5 - Closed"]
NAME = {s: s.split(" - ", 1)[1] for s in STAGES}

# action: (allowed from, target stage, required values, properties written)
ACTIONS = {
    "ready": ({"Building"}, "Ready", [], []),
    "posted": ({"Building", "Ready"}, "Posted", ["price", "date"], ["posted_price", "posted_date"]),
    "price": ({"Posted"}, "Posted", ["price"], ["posted_price"]),
    "sold": ({"Posted"}, "Sold", ["price", "date"], ["sold_price", "sold_date"]),
    "closed": ({"Building", "Ready", "Posted"}, "Closed", [], []),
}


def out(code: int, **payload) -> None:
    print(json.dumps(payload, indent=2))
    sys.exit(code)


def find_workspace(start: Path) -> Path | None:
    for path in [start, *start.parents]:
        if (path / "Dashboard.base").is_file() and (path / "Listings").is_dir():
            return path
    return None


def all_items(listings: Path) -> list[Path]:
    return [p for s in STAGES if (listings / s).is_dir() for p in sorted((listings / s).iterdir())
            if p.is_dir() and (p / "Listing.md").is_file()]


def resolve(listings: Path, item: str) -> list[Path]:
    given = Path(item).expanduser()
    if given.name == "Listing.md":
        given = given.parent
    if given.is_absolute() and (given / "Listing.md").is_file():
        return [given]
    items = all_items(listings)
    key = item.strip().casefold()
    exact = [p for p in items if p.name.casefold() == key]
    if exact:
        return exact
    return [p for p in items if key in p.name.casefold()]


def parse_price(raw: str) -> str:
    cleaned = raw.replace("$", "").replace(",", "").strip()
    try:
        value = float(cleaned)
    except ValueError:
        out(4, status="error", message=f"Price is not a number: {raw!r}")
    return str(int(value)) if value == int(value) else f"{value:.2f}"


def parse_date(raw: str) -> str:
    if raw.strip().lower() == "today":
        return dt.date.today().isoformat()
    try:
        return dt.date.fromisoformat(raw.strip()).isoformat()
    except ValueError:
        out(4, status="error", message=f"Date must be YYYY-MM-DD or 'today': {raw!r}")


def read_props(text: str) -> tuple[dict[str, str], re.Match]:
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        out(5, status="error", message="Listing.md has no YAML frontmatter")
    props = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            props[key.strip()] = value.strip().strip("'\"")
    return props, match


def write_props(text: str, match: re.Match, updates: dict[str, str]) -> str:
    lines = match.group(1).splitlines()
    for key, value in updates.items():
        pattern = re.compile(rf"^{re.escape(key)}:.*$")
        for i, line in enumerate(lines):
            if pattern.match(line):
                lines[i] = f"{key}: {value}"
                break
        else:
            lines.append(f"{key}: {value}")
    return "---\n" + "\n".join(lines) + "\n---\n" + text[match.end():]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--workspace", help="Workspace folder; defaults to searching upward from the current folder")
    ap.add_argument("--item", required=True, help="Item folder name, part of it, or a path to the item folder or Listing.md")
    ap.add_argument("--action", required=True, choices=sorted(ACTIONS))
    ap.add_argument("--price")
    ap.add_argument("--date", help="YYYY-MM-DD or 'today'")
    ap.add_argument("--approved", action="store_true", help="Seller approved a correction, reopening, or unusual transition")
    args = ap.parse_args()

    workspace = Path(args.workspace).expanduser() if args.workspace else find_workspace(Path.cwd())
    if not workspace or not (workspace / "Listings").is_dir():
        out(5, status="error", message="No initialized workspace found; pass --workspace")
    listings = workspace / "Listings"

    matches = resolve(listings, args.item)
    if len(matches) != 1:
        out(2, status="not_found" if not matches else "ambiguous",
            candidates=[str(p.relative_to(workspace)) for p in matches])
    folder = matches[0]
    current = NAME.get(folder.parent.name)
    if current is None:
        out(5, status="error", message=f"Item is not inside a lifecycle folder: {folder}")

    allowed, target, required, keys = ACTIONS[args.action]
    supplied = {"price": args.price, "date": args.date}
    missing = [r for r in required if not supplied[r]]
    if missing:
        out(4, status="missing", missing=missing, item=folder.name, current=current)
    values = {}
    if "price" in required:
        values["price"] = parse_price(args.price)
    if "date" in required:
        values["date"] = parse_date(args.date)
    updates = dict(zip(keys, [values[r] for r in required]))

    note = folder / "Listing.md"
    text = note.read_text(encoding="utf-8")
    props, match = read_props(text)
    recorded = {k: props.get(k, "") for k in updates}
    conflicts = {k: {"recorded": recorded[k], "requested": v}
                 for k, v in updates.items() if recorded[k] and recorded[k] != v}

    if current == target and args.action != "price":
        if not conflicts:
            out(0, status="already_current", item=folder.name, stage=current,
                path=str(folder.relative_to(workspace)))
        if not args.approved:
            out(3, status="needs_approval", reason="correction", item=folder.name,
                stage=current, conflicts=conflicts)
    elif current not in allowed and not args.approved:
        out(3, status="needs_approval", reason="unusual_transition", item=folder.name,
            current=current, requested=target)

    stage_dir = next(s for s in STAGES if NAME[s] == target)
    destination = listings / stage_dir / folder.name
    if destination != folder and destination.exists():
        out(5, status="error", message=f"Target folder already exists: {destination.relative_to(workspace)}")

    if updates:
        note.write_text(write_props(text, match, updates), encoding="utf-8")
    if destination != folder:
        destination.parent.mkdir(exist_ok=True)
        folder.rename(destination)

    out(0, status="applied", item=destination.name, from_stage=current, stage=target,
        written=updates, path=str(destination.relative_to(workspace)))


if __name__ == "__main__":
    main()
