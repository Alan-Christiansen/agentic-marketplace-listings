---
name: new-listing
description: Start one Facebook Marketplace or eBay listing in an initialized Agentic Marketplace Listings workspace, creating its Building folder and Listing.md before pausing for photos by default, then prepare it after the seller confirms the photos are ready or explicitly says there are none. Do not use for cross-posting, external posting, or updating an ambiguous existing listing.
---
# Marketplace: New Listing
Start with a stable place for working photos, then turn the seller's available evidence into one organized listing while asking as little as accuracy permits.
## Stage 1: Create the intake record and pause
Find the intended workspace by the presence of `How to Use.md`, `Dashboard.base`, the platform templates, and the five lifecycle folders. If it is not initialized, recommend the plugin's `setup` skill and stop.

Resolve a concise human-readable item name and exactly one platform: Facebook Marketplace or eBay. If the seller has not selected a platform, ask before creating the source record. For eBay, determine whether an applicable category-specific template exists. Ask when the available information does not safely distinguish the general eBay template from a specialized template.

Choose one template before running the preflight:
- Facebook Marketplace: `Platforms/Facebook/Listing Template.md`.
- eBay Stamps, including first-day covers and other items whose primary collectible is a stamp or postal issue: `Platforms/eBay/Categories/Stamps/Listing Template.md`.
- Other eBay items: `Platforms/eBay/Listing Template.md` unless another applicable specialized template exists.

Ask which eBay template applies only when that choice would materially change the fields and the request does not resolve it.

Treat routine Stage 1 intake in an initialized workspace as self-contained. Do not search provider memory, project history, prior listings, or web sources. Do not load the contents of `How to Use.md` or `Dashboard.base`, platform guidance, seller profiles, or photos.

Use one read-only preflight tool call to read the plugin's [operating policy](../../references/operating-policy.md) and the selected template, verify the workspace markers, and search all lifecycle folders for a same-named item or likely duplicate. Do not split these checks into separate calls.

If a same-named item folder or likely duplicate exists anywhere in the lifecycle folders, show the candidates and ask whether to use the existing listing or choose another name. Do not create a suffixed duplicate silently.

The seller's request to start a listing authorizes creation of `Listings/1 - Building/<Item name>/Listing.md`; do not pause for a separate approval after a clean preflight. Create it from the selected template, set the item name and local creation date as an unquoted `YYYY-MM-DD` property value, and place supplied notes, features, dimensions, and item facts in the matching intake sections without discarding uncertainty or changing their meaning. Preserve the template's compact ATX-heading spacing exactly: do not insert a blank line immediately before or after any heading.

Working photos belong beside `Listing.md`. Do not create an originals folder, relocate an external original library, or silently alter image files.

Unless the seller explicitly says there will be no photos, report the exact item-folder path for photo export and stop. A successful creation tool result is sufficient verification; make a separate existence or content-check call only when the creation result is missing, ambiguous, or reports an error. Do not add another planning or status message between a clean preflight and creation. Do not identify the item, research it, load drafting guidance, or fill platform-ready fields during this first stage.
## Stage 2: Prepare after photos
Continue only after the seller confirms the photos are in the item folder or explicitly says there are no photos. If photos were expected but none are present, report that and remain paused. Use co-located working photos without modifying them.

Load only:
1. `Platforms/Facebook/Guidance.md` or `Platforms/eBay/Guidance.md` for the selected platform;
2. `Platforms/Facebook/Seller Profile.md` or `Platforms/eBay/Seller Profile.md` for the selected platform;
3. applicable category guidance, such as `Platforms/eBay/Categories/Stamps/Guidance.md`;
4. the current item note and its co-located photos.

Use approved examples inside the seller profile only for voice and structure. Never transfer their facts, prices, condition claims, or category details to the current item.

Identify the item and research only when useful or requested. Separate seller facts, visible evidence, research, and inference. For stamps, preserve seller-entered specialist data and never invent catalog number, issue, variety, grade, gum condition, cancellation, faults, or authenticity. Keep unsupported stamp fields blank or explicitly unknown, and do not conflate Place of Origin with Country of Origin.

Draft each platform-ready field under the headings supplied by the selected template. Preserve blanks or explicit unknowns when information is incomplete but a useful draft is still possible. When editing the record, keep the template's compact ATX-heading spacing: no blank line immediately before or after a heading. Ask a compact grouped question only for remaining blockers.
## Finish preparation
The live `Dashboard.base` needs no regeneration. Keep the item in Building until the seller confirms the content is ready; then move its whole folder to Ready. Do not claim the listing was posted or move it to Posted without a separate explicit instruction containing the actual posted price or confirming the prepared price.

Report the exact listing path, what was prepared, any unresolved facts, and the smallest useful next action. Never post externally, contact buyers, accept an offer, or create a second platform copy.
