# How to Use Marketplace Listings
This folder is a lightweight Obsidian workspace for preparing and tracking items sold through Facebook Marketplace or eBay. Each listing is an ordinary folder with one `Listing.md` note and any working photos placed beside it. Open `Dashboard.base` for the live overview.
## Start a listing
Invoke `Marketplace: new-listing` and provide whatever you already know. A rough name, free-form notes, a feature list, or dimensions are enough to begin. Choose Facebook Marketplace or eBay before the listing record is created. For eBay, the agent will use a category-specific template when one is available and applicable.

The agent first creates the item folder and `Listing.md`, gives you the exact folder path, and pauses. Export the working photos into that folder, then tell the agent they are ready so it can identify, research, price, and draft the listing. This pause happens automatically for every new listing. If you do not have photos, say so and the agent will continue without them.
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
Invoke `Marketplace: update-listing` and name the item plus the change. A complete request is handled in one turn without a second confirmation: for example, “Mark the oak dresser Ready,” “I posted the oak dresser for $125 today,” “Change the dresser's price to $110,” “It sold for $90 today,” or “Close the dresser; it didn't sell.” Posted requires the actual price and date, a price change requires the new price, and Sold requires the actual price and date. If something required is missing, the agent asks one compact follow-up. The skill updates the listing properties and moves the whole item folder; the Base reflects those changes automatically.
## Customize the writing
Edit the matching `Seller Profile.md` under `Platforms/Facebook/` or `Platforms/eBay/` to describe your desired voice, recurring practices, and approved examples. These files belong to you and should not be overwritten by engine updates.
