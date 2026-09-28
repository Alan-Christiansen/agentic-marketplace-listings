---
name: marketplace-new-listing
description: Start one Facebook Marketplace or eBay listing in an initialized Agentic Marketplace Listings workspace, creating its Building folder and Listing.md before pausing for photos by default, then prepare it after the seller confirms the photos are ready or explicitly says there are none. Do not use for cross-posting, external posting, or updating an ambiguous existing listing.
---
# Marketplace: New Listing
Turn the seller's notes and photos into one accurate listing record, asking only what accuracy requires. Follow the plugin's [operating policy](../../references/operating-policy.md).
## 1. Create the record
- Confirm the workspace is initialized.
- Resolve a short, human-readable item name and one platform: Facebook Marketplace or eBay. Ask if the platform is not given.
- Choose the template:
  - Facebook Marketplace: `Platforms/Facebook/Listing Template.md`.
  - eBay stamps, first-day covers, and other items whose main collectible is a stamp or postal issue: `Platforms/eBay/Categories/Stamps/Listing Template.md`.
  - Other eBay items: `Platforms/eBay/Listing Template.md`, unless another folder under `Platforms/eBay/Categories/` fits. Ask only when the choice is unclear and would change the fields.
- If an item folder with the same or a very similar name exists in any lifecycle folder, show it and ask whether to use it or choose another name. Never create a suffixed duplicate.
- Create `Listings/1 - Building/<Item name>/Listing.md` from the template. Fill the item name, the `created` date, and the seller's notes, features, and dimensions in the intake sections without changing their meaning. The request to start a listing is approval for this write.
## 2. Photos
Unless the seller said there will be no photos, report the item-folder path so the seller can export working photos there, and stop. Continue when the seller says the photos are in place. If none are present, say so and stay paused.
## 3. Prepare
Read the platform's `Guidance.md` and `Seller Profile.md`, any applicable category `Guidance.md`, and the photos. Identify the item, research when useful, and draft each platform field under the template's headings. Put evidence and uncertainty in `Photo-Derived Observations` and `Research Notes`, not in buyer-facing fields. Ask one grouped question only for real blockers.
## 4. Finish
Keep the item in Building. Report the listing path, what was prepared, any unresolved facts, and the next step, usually a review followed by marking it Ready. Move it to Ready only when the seller says the draft is ready.
