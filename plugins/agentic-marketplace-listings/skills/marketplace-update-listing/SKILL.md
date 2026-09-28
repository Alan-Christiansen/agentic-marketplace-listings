---
name: marketplace-update-listing
description: Update one existing Agentic Marketplace Listings record through Ready, Posted, price-change, Sold, or Closed lifecycle actions. Use when the seller wants to change the state or tracked posted or sold details of a known listing. Do not use for external posting, buyer communication, bookkeeping, or an ambiguous listing.
---
# Marketplace: Update Listing
Record one lifecycle change with one script call. Do not read `Listing.md`, the operating policy, guidance, or the dashboard first; the script resolves the listing and checks everything.
## Run
Run the workspace copy of the script, in the same shell that can see the vault:
```sh
python3 "<workspace>/.scripts/update_listing.py" --item "<item name or path>" --action <action> [--price <number>] [--date <YYYY-MM-DD|today>] --workspace "<workspace>"
```
- If `.scripts/update_listing.py` is missing, use `<this skill's directory>/scripts/update_listing.py` when it can run where the vault is, and tell the seller to rerun setup to install the workspace copy.
- Never paste or encode the script into a remote shell. If neither copy can run where the vault is, use the manual fallback below.
- On `not_found`, list the item folder names under `Listings/*/` before asking. The seller may have misspelled the name or used a partial one, so pick the obvious match and rerun with its path.

| Action | Moves | Needs |
| --- | --- | --- |
| `ready` | Building to Ready | Nothing |
| `posted` | Building or Ready to Posted | Price and date |
| `price` | Stays in Posted | New price |
| `sold` | Posted to Sold | Price and date |
| `closed` | Building, Ready, or Posted to Closed | Nothing |

- Pass `--workspace` unless the current folder is inside the workspace.
- Pass `--date today` only when the seller said today. Never assume a date.
- Recording Posted means the seller already posted it. Never post to a marketplace.
## Act on the result
- Exit 0 (`applied` or `already_current`): report the status, recorded values, and path in one or two lines. Stop.
- Exit 2 (`not_found` or `ambiguous`): if exactly one folder is an obvious match, rerun with its path. Otherwise show the candidates, ask which one, then rerun.
- Exit 3 (`needs_approval`): show the conflict or unusual transition and ask. If the seller approves, rerun with `--approved`.
- Exit 4 (`missing`): ask one question for the missing values, then rerun.
- Exit 5: report the message and stop.
## Manual fallback
Use this when Python is unavailable or no copy of the script can run where the vault is. Make the same change by hand: set only the properties in the table's action in the `Listing.md` frontmatter (unquoted `YYYY-MM-DD` dates, numeric prices), then move the whole item folder to the target lifecycle folder.
