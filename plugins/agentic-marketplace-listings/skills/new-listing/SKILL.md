---
name: new-listing
description: Start and prepare one Facebook Marketplace or eBay listing in an initialized Agentic Marketplace Listings workspace. Use when the seller wants to create a listing from rough notes, item facts, and photos. Do not use for cross-posting, external posting, or updating an ambiguous existing listing.
---
# AML: New Listing
Turn whatever the seller already has into one organized listing while asking as little as accuracy permits.
## Locate the workspace and item
Find the intended workspace by its `How to Use.md`, `Dashboard.base`, `Platforms/Facebook/Listing Template.md`, `Platforms/eBay/Listing Template.md`, and lifecycle folders. If it is not initialized, recommend `$agentic-marketplace-listings:setup` and stop.

Read the plugin's [operating policy](../../references/operating-policy.md). Resolve a concise human-readable item name and exactly one platform: Facebook Marketplace or eBay. If the seller has not selected a platform, ask before creating the source record. For eBay, determine whether an applicable category-specific template exists. Ask when the available information does not safely distinguish the general eBay template from a specialized template.

If a same-named item folder or likely duplicate exists anywhere in the lifecycle folders, show the candidates and ask whether to use the existing listing or choose another name. Do not create a suffixed duplicate silently.
## Create the source record
Choose one template:
- Facebook Marketplace: `Platforms/Facebook/Listing Template.md`.
- eBay without an applicable specialized template: `Platforms/eBay/Listing Template.md`.
- eBay Stamps: `Platforms/eBay/Categories/Stamps/Listing Template.md`.

Create `Listings/1 - Building/<Item name>/Listing.md` from the selected template. Set the item name and local creation date, written as an unquoted `YYYY-MM-DD` property value. Incorporate the seller's rough notes, features, dimensions, item facts, and photo observations into the matching intake sections without discarding uncertainty or changing their meaning.

Working photos belong beside `Listing.md`. Use photos already there or explicitly supplied for the item. Do not create an originals folder, relocate an external original library, or silently alter image files.
## Prepare the listing
Load only:
1. `Platforms/Facebook/Guidance.md` or `Platforms/eBay/Guidance.md` for the selected platform;
2. `Platforms/Facebook/Seller Profile.md` or `Platforms/eBay/Seller Profile.md` for the selected platform;
3. applicable category guidance, such as `Platforms/eBay/Categories/Stamps/Guidance.md`;
4. the current item note and its co-located photos.

Use approved examples inside the seller profile only for voice and structure. Never transfer their facts, prices, condition claims, or category details to the current item.

Identify the item and research only when useful or requested. Separate seller facts, visible evidence, research, and inference. For stamps, preserve seller-entered specialist data and never invent catalog number, issue, variety, grade, gum condition, cancellation, faults, or authenticity. Keep unsupported stamp fields blank or explicitly unknown, and do not conflate Place of Origin with Country of Origin.

Draft each platform-ready field under the headings supplied by the selected template. Preserve blanks or explicit unknowns when information is incomplete but a useful draft is still possible. Ask a compact grouped question only for remaining blockers.
## Finish the turn
The live `Dashboard.base` needs no regeneration. Keep the item in Building until the seller confirms the content is ready; then move its whole folder to Ready. Do not claim the listing was posted or move it to Posted without a separate explicit instruction containing the actual posted price or confirming the prepared price.

Report the exact listing path, what was prepared, any unresolved facts, and the smallest useful next action. Never post externally, contact buyers, accept an offer, or create a second platform copy.
