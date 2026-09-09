# Agentic Marketplace Listings
Selling usually starts with an untidy mix of photos, rough notes, measurements, and half-remembered details. Turning that material into a trustworthy listing, then remembering what is ready, posted, sold, or closed, is often more work than the item is worth.

> Agentic Marketplace Listings gives ChatGPT/Codex or Claude Cowork a small set of workflows for preparing and tracking Facebook Marketplace and eBay listings in Obsidian. Your listings remain ordinary Markdown files, and an Obsidian Base provides a live dashboard without creating a second data store.
## How to use
### Set up the workspace
Ask the agent to set up Marketplace Listings in a folder inside your Obsidian vault. It shows the exact files it will create or update and waits for approval before writing anything.

The resulting workspace includes platform guidance, editable seller profiles, listing templates, five lifecycle folders, and a live `Dashboard.base` overview. Obsidian's Bases core plugin must be enabled.
### Review and customize the guidance
Before preparing your first listing, review the `Guidance.md` and `Seller Profile.md` files for each platform you plan to use. Adjust them to match your needs, including your approach to research, pricing, listing content, and recurring selling practices.

Pay special attention to `Voice and tone` in each seller profile. Make sure it sounds like you, then review every finished draft before posting to confirm that the wording fits your voice and accurately represents the item.

Seller profiles are always preserved during setup updates. If you customize a `Guidance.md` file, review future update proposals carefully so you do not unintentionally replace your changes.
### Start a listing
1. Ask the agent to start a Facebook Marketplace or eBay listing and provide whatever you already know.
2. The agent creates a named folder with `Listing.md`, gives you its exact location, and pauses.
3. Export working photos into that folder and tell the agent they are ready. If there will be no photos, say so.
4. The agent uses your notes, photos, platform guidance, and seller profile to prepare the listing without inventing missing facts.

For eBay, category-specific guidance is used when available, beginning with stamps and first-day covers.
### Track the listing
Tell the agent when an item is ready, posted, repriced, sold, or closed. It records the applicable price and date, moves the complete item folder, and leaves the Base dashboard to update automatically.

The lifecycle remains visible in ordinary folders:

- `1 - Building`
- `2 - Ready`
- `3 - Posted`
- `4 - Sold`
- `5 - Closed`
## Installation
### ChatGPT and Codex
Add this repository as a Codex marketplace, install the plugin, then start a new task:
```sh
codex plugin marketplace add Alan-Christiansen/agentic-marketplace-listings --ref main
codex plugin add agentic-marketplace-listings@agentic-marketplace-listings
```

The available skills are shown as `Marketplace: setup`, `Marketplace: new-listing`, and `Marketplace: update-listing`.
### Claude Cowork
1. Open Cowork, then open **Customize → Plugins**.
2. In **Personal plugins**, select **+ → Add marketplace**.
3. Add `https://github.com/Alan-Christiansen/agentic-marketplace-listings` as a repository.
4. Install **Agentic Marketplace Listings** and begin a new Cowork task.

In Claude, the skills are namespaced under `agentic-marketplace-listings` and can also be selected from the skills menu.
## Get updates
### ChatGPT and Codex
Refresh the Git-backed marketplace and reinstall the plugin:
```sh
codex plugin marketplace upgrade agentic-marketplace-listings
codex plugin add agentic-marketplace-listings@agentic-marketplace-listings
```
### Claude Cowork
Refresh the marketplace from the Plugins screen, then update or reinstall the plugin when Claude shows a newer version.

Run the setup skill against the existing workspace to review engine-file updates. It will show the exact proposed replacements before writing them.
## Compatibility and limitations
- Requires a file-capable ChatGPT/Codex or Claude Cowork session with access to the selected workspace folder.
- Requires Obsidian with the Bases core plugin enabled.
- Supports Facebook Marketplace and eBay, with specialized eBay support beginning with stamps.
- Each listing targets one platform. Cross-posting is not included.
- Tracks posted and sold prices, not fees, shipping costs, or net proceeds.
- Does not post externally, contact buyers, accept offers, or make pricing commitments.
## Privacy and ownership
The plugin has no accounts, analytics, background network service, or bundled personal seller data. It reads and writes only through the host agent's approved file access and uses web research only when useful or requested during listing preparation.

Seller profiles, listings, photos, and sale records belong to you. Setup updates show an exact preflight and never overwrite seller profiles or live listing data. Review any AI-prepared listing before posting it.
## Support and contributing
Use [GitHub Issues](https://github.com/Alan-Christiansen/agentic-marketplace-listings/issues) for bug reports and feature suggestions. Small fixes and documentation improvements are welcome as pull requests; please open an issue before starting a substantial workflow or behavior change. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

Created and maintained by Alan Christiansen under Spectra Studio.

Agentic Marketplace Listings is available under the [MIT License](LICENSE).
