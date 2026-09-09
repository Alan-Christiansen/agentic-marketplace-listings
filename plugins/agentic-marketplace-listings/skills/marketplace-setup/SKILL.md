---
name: marketplace-setup
description: Create or safely update a self-contained Agentic Marketplace Listings workspace in a user-selected Obsidian vault folder. Use when the user asks to set up, initialize, install, or refresh the selling workspace. Do not use to create an individual listing or install the host plugin itself.
---
# Marketplace: Setup
Create an Obsidian workspace with ordinary Markdown listing records and a live Base dashboard. It has no dependency on private vault infrastructure.
## Establish the target
Resolve one exact destination folder from the user's request or active workspace. Do not choose a vault root, project folder, or similarly named destination when more than one is plausible. If the destination is ambiguous, ask one concise question.

Read the plugin's [operating policy](../../references/operating-policy.md) and the bundled files under `assets/workspace/` before proposing changes.
## Inspect before writing
Determine whether this is a first setup or an update. Inspect the exact destination, applicable local agent instructions, filename and case collisions, existing lifecycle folders, and any seller-owned material.

Present a compact preflight containing:
- the exact destination;
- whether the operation is initialization or update;
- every file and folder to create;
- every engine-owned file proposed for replacement;
- every existing seller-owned file that will be preserved;
- conflicts or uncertain ownership;
- the stop boundary: no listing creation, plugin installation, external posting, deletion, or unrelated vault changes.

Obtain explicit approval for that write set. If the destination or mutation set changes, refresh the affected preflight.
## Create or update the workspace
On first setup:
1. Copy the bundled `How to Use.md`, `Dashboard.base`, and `Platforms/**` files into the destination without overwriting collisions.
2. Create `Listings/1 - Building`, `Listings/2 - Ready`, `Listings/3 - Posted`, `Listings/4 - Sold`, and `Listings/5 - Closed`.

On update:
- Entry-note rename: when an existing workspace contains `Marketplace Listings.md` but not `How to Use.md`, propose renaming it in the preflight and perform the rename only when approved. If both files exist, stop and show the conflict.
- Engine-owned: replace `How to Use.md`, `Platforms/**/Guidance.md`, and `Platforms/**/Listing Template.md` only when each replacement appeared in the approved write set.
- Seller-owned: never overwrite `Platforms/*/Seller Profile.md`, `Listings/**`, listing notes, or photos. Create a missing bundled seller profile only after identifying it in the preflight.
- Base dashboard: replace `Dashboard.base` only when that replacement appeared in the approved write set. If a legacy `Dashboard.md` exists, preserve it unless its removal appeared in the approved write set.
- Create missing lifecycle folders; never move or delete listing folders during setup.

When migrating a workspace that still uses `Seller Profiles/**` and `System/**`, treat every legacy seller profile as seller-owned. Move it to the matching `Platforms/<Platform>/Seller Profile.md` only when that move appeared in the approved write set and the destination does not already contain a profile. If both locations contain a profile, stop and show the conflict. Remove superseded engine files or empty legacy folders only when their removal appeared in the approved write set and the replacement files have been verified.

Do not claim rollback if a write partially fails. Stop, preserve the recoverable state, and report exactly what succeeded and failed.
## Validate and stop
Verify that all five lifecycle folders exist; `Dashboard.base` is readable; the Facebook, general eBay, and eBay Stamps templates and guidance files are readable; both platform seller-profile files exist; seller-owned files were preserved; and no unresolved template tokens appear outside files named `Listing Template.md`. Report the created, updated, removed, and preserved paths. Stop without creating a listing or beginning operational selling work.
