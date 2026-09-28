---
name: marketplace-new-listing
description: Start and prepare one Facebook Marketplace or eBay listing in an initialized Agentic Marketplace Listings workspace from the seller's notes and attached photos, creating its Building folder and Listing.md, saving the photos beside it, and drafting the listing in the same turn. If no photos are attached, it asks for them first. Do not use for cross-posting, external posting, or updating an existing listing.
---
# Marketplace: New Listing
Turn one message of seller notes and photos into one accurate listing record, asking only what accuracy requires. Follow the plugin's [operating policy](../../references/operating-policy.md).
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
- **Photos attached to the request:** save each one into the item folder beside `Listing.md` as `photo-01`, `photo-02`, and so on in the order attached, keeping each file's extension and continuing the numbering if photos already exist. Save them as received, then continue to Prepare in the same turn.
- **Photos already in the item folder, or the seller says there will be no photos:** continue to Prepare.
- **Otherwise:** report the item-folder path, ask the seller to attach the photos in their next message or put them in that folder, and stop. When they arrive, save them as above and continue.

If the host cannot save attached images as files in the workspace, say so once, give the folder path, and ask the seller to put the photos there.
## 3. Prepare
Read the platform's `Guidance.md` and `Seller Profile.md`, any applicable category `Guidance.md`, and the photos. Identify the item, research when useful, and draft each platform field under the template's headings. Put evidence and uncertainty in `Photo-Derived Observations` and `Research Notes`, not in buyer-facing fields. Ask one grouped question only for real blockers.
## 4. Finish
Keep the item in Building. Report the listing path, what was prepared, any unresolved facts, and the next step, usually a review followed by marking it Ready. Move it to Ready only when the seller says the draft is ready.
