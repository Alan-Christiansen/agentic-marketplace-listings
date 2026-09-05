#!/usr/bin/env python3
"""Validate the Agentic Marketplace Listings repository without dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "agentic-marketplace-listings"
WORKSPACE = PLUGIN / "skills" / "setup" / "assets" / "workspace"


def fail(message: str) -> None:
    raise ValueError(message)


def read(path: Path) -> str:
    if not path.is_file():
        fail(f"Missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict:
    try:
        return json.loads(read(path))
    except json.JSONDecodeError as exc:
        fail(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")


def validate_manifest() -> None:
    manifest = load_json(PLUGIN / ".codex-plugin" / "plugin.json")
    if manifest.get("name") != "agentic-marketplace-listings":
        fail("Plugin manifest name does not match the plugin folder")
    if manifest.get("skills") != "./skills/":
        fail("Plugin manifest must point skills to ./skills/")
    if manifest.get("license") != "MIT":
        fail("Plugin manifest must declare the MIT license")


def validate_marketplace() -> None:
    marketplace = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    if marketplace.get("name") != "agentic-marketplace-listings":
        fail("Marketplace name must be agentic-marketplace-listings")
    entries = marketplace.get("plugins", [])
    if len(entries) != 1 or entries[0].get("name") != "agentic-marketplace-listings":
        fail("Marketplace must contain exactly the AML plugin entry")
    if entries[0].get("source", {}).get("path") != "./plugins/agentic-marketplace-listings":
        fail("Marketplace plugin path is incorrect")


def validate_skills() -> None:
    expected = {"setup", "new-listing", "update-listing"}
    skill_dirs = {path.parent.name for path in (PLUGIN / "skills").glob("*/SKILL.md")}
    if skill_dirs != expected:
        fail(f"Unexpected skill set: {sorted(skill_dirs)}")
    for name in expected:
        text = read(PLUGIN / "skills" / name / "SKILL.md")
        if not text.startswith("---\n") or f"name: {name}\n" not in text:
            fail(f"Invalid skill frontmatter for {name}")
        read(PLUGIN / "skills" / name / "agents" / "openai.yaml")

    new_listing = read(PLUGIN / "skills" / "new-listing" / "SKILL.md")
    fast_path_requirements = {
        "self-contained Stage 1": "Treat routine Stage 1 intake in an initialized workspace as self-contained.",
        "single preflight call": "Use one read-only preflight tool call",
        "no split preflight": "Do not split these checks into separate calls.",
        "first-day cover routing": "including first-day covers",
        "successful creation verification": "A successful creation tool result is sufficient verification",
        "no post-preflight narration": "Do not add another planning or status message between a clean preflight and creation.",
    }
    for requirement, token in fast_path_requirements.items():
        if token not in new_listing:
            fail(f"New-listing skill is missing the {requirement} fast-path contract")


def validate_workspace() -> None:
    required = [
        "How to Use.md",
        "Dashboard.base",
        "Platforms/Facebook/Seller Profile.md",
        "Platforms/Facebook/Guidance.md",
        "Platforms/Facebook/Listing Template.md",
        "Platforms/eBay/Seller Profile.md",
        "Platforms/eBay/Guidance.md",
        "Platforms/eBay/Listing Template.md",
        "Platforms/eBay/Categories/Stamps/Guidance.md",
        "Platforms/eBay/Categories/Stamps/Listing Template.md",
    ]
    for relative in required:
        read(WORKSPACE / relative)
    if (WORKSPACE / "Dashboard.md").exists():
        fail("Legacy Dashboard.md must not be bundled")

    base = read(WORKSPACE / "Dashboard.base")
    for token in ["file.basename", "formula.item", "formula.status", "time_to_sell", "views:"]:
        if token not in base:
            fail(f"Dashboard.base is missing {token}")

    expected_keys = [
        "type",
        "platform",
        "created",
        "posted_price",
        "posted_date",
        "sold_price",
        "sold_date",
    ]
    templates = list(WORKSPACE.glob("Platforms/**/Listing Template.md"))
    if len(templates) != 3:
        fail(f"Expected three listing templates, found {len(templates)}")
    for template in templates:
        text = read(template)
        match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
        if not match:
            fail(f"Missing YAML frontmatter in {template.relative_to(ROOT)}")
        keys = [line.split(":", 1)[0] for line in match.group(1).splitlines() if ":" in line]
        if keys != expected_keys:
            fail(f"Unexpected property order in {template.relative_to(ROOT)}: {keys}")


def validate_public_safety() -> None:
    forbidden = ["/Users/", "_Vaults/", "Studio-Vault", "alanc/"]
    placeholders = ["[TODO:", "TODO:"]
    text_files = [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and path.resolve() != Path(__file__).resolve()
    ]
    for path in text_files:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for value in forbidden:
            if value in text:
                fail(f"Private local path fragment {value!r} in {path.relative_to(ROOT)}")
        for value in placeholders:
            if value in text:
                fail(f"Unfinished placeholder {value!r} in {path.relative_to(ROOT)}")


def main() -> int:
    checks = [
        validate_manifest,
        validate_marketplace,
        validate_skills,
        validate_workspace,
        validate_public_safety,
    ]
    try:
        for check in checks:
            check()
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("Validated Agentic Marketplace Listings repository")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
