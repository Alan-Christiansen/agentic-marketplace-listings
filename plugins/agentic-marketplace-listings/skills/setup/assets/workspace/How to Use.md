# How to Use Marketplace Listings
This folder is a lightweight Obsidian workspace for preparing and tracking items sold through Facebook Marketplace or eBay. Each listing is an ordinary folder with one `Listing.md` note and any working photos placed beside it. Open `Dashboard.base` for the live overview.
## Start a listing
Invoke `AML: new-listing` and provide whatever you already know. A rough name, free-form notes, a feature list, dimensions, or a set of photos is enough to begin. Choose Facebook Marketplace or eBay before the listing record is created. For eBay, the agent will use a category-specific template when one is available and applicable.
## Lifecycle
- `1 - Building` — information or drafting is still in progress.
- `2 - Ready` — the listing is prepared and ready for you to post.
- `3 - Posted` — the listing is live.
- `4 - Sold` — the item sold.
- `5 - Closed` — the listing ended without a sale, including removed, expired, or donated items.

The listing's parent folder is its status. Move the whole item folder when the status changes; do not duplicate status inside the note.
## What is tracked
V1 records the selected platform, posted price and date, and sold price and date. It does not track selling fees, shipping costs, net proceeds, or cross-posting.
## Update a listing
Invoke `AML: update-listing` to mark a draft Ready, record that it was Posted, change its current posted price, record a sale, or close it without a sale. The skill updates the listing properties and moves the whole item folder. The Base reflects those changes automatically.
## Customize the writing
Edit the matching `Seller Profile.md` under `Platforms/Facebook/` or `Platforms/eBay/` to describe your desired voice, recurring practices, and approved examples. These files belong to you and should not be overwritten by engine updates.
