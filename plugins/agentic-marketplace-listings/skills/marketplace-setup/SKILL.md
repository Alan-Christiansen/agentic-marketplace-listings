---
name: marketplace-setup
description: Create or safely update a self-contained Agentic Marketplace Listings workspace in a user-selected Obsidian vault folder. Use when the user asks to set up, initialize, install, or refresh the selling workspace. Do not use to create an individual listing or install the host plugin itself.
---
# Marketplace: Setup
Create or update a Marketplace Listings workspace in one folder the user chooses. Follow the plugin's [operating policy](../../references/operating-policy.md).
## Target
Resolve one exact destination folder. If more than one folder is plausible, ask. Never default to a vault root.
## Preflight
Compare the bundled files in `assets/workspace/` with the destination and show:
- the destination, and whether this is a new setup or an update;
- files and folders to create;
- engine files to replace, listing only those that differ: `How to Use.md`, `Dashboard.base`, `Platforms/**/Guidance.md`, `Platforms/**/Listing Template.md`;
- seller files that will be preserved: `Platforms/*/Seller Profile.md` and everything under `Listings/`;
- conflicts or unclear ownership.

Wait for explicit approval. If the write set changes, show it again.

If the destination uses an older layout, such as `Seller Profiles/` or `System/` folders, report it as a conflict and stop. Do not migrate it.
## Write
- Copy the approved bundled files. Never overwrite a seller profile; create a missing one only if the preflight listed it.
- Create any missing lifecycle folders under `Listings/`.
- Never move, rename, or delete listing folders or photos.
- If a write fails, stop and report exactly what succeeded and what did not. Do not claim a rollback.
## Verify
Confirm the five lifecycle folders exist, the bundled files are readable, and seller files are unchanged. Report the created, replaced, and preserved paths, then stop without creating a listing.
