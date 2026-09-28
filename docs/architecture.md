# Architecture
## Design goal
Agentic Marketplace Listings should make selling feel like working with a capable assistant, not maintaining an inventory application. The seller supplies rough facts and photos; the agent handles repeatable organization and drafting while leaving every durable listing record readable as ordinary Markdown.
## Obsidian workspace
```text
Marketplace Listings/
├── How to Use.md
├── Dashboard.base
├── Platforms/
│   ├── Facebook/
│   │   ├── Seller Profile.md
│   │   ├── Guidance.md
│   │   └── Listing Template.md
│   └── eBay/
│       ├── Seller Profile.md
│       ├── Guidance.md
│       ├── Listing Template.md
│       └── Categories/
│           └── Stamps/
│               ├── Guidance.md
│               └── Listing Template.md
└── Listings/
    ├── 1 - Building/
    ├── 2 - Ready/
    ├── 3 - Posted/
    ├── 4 - Sold/
    └── 5 - Closed/
```

Each item has a human-named folder containing `Listing.md` and any working photos. The parent lifecycle folder is the authoritative status; the listing does not duplicate status in metadata.

## Ownership boundary
| Content | Owner | Update behavior |
| --- | --- | --- |
| `How to Use.md` | Engine | May be refreshed after review |
| `Platforms/**/Guidance.md` | Engine | May be refreshed after review |
| `Platforms/**/Listing Template.md` | Engine | May be refreshed after review |
| `Platforms/*/Seller Profile.md` | Seller | Create only when absent; never overwrite |
| `Listings/**` and photos | Seller | Never overwrite or delete |
| `Dashboard.base` | Engine | Live derived view; may be refreshed after review |

The setup skill must identify collisions and show the exact update set before replacing engine-owned files. Updates never overwrite seller-owned content.
## Information layers
Rules live in one place each. `references/operating-policy.md` owns sources of truth, fact integrity, record formats, and authority boundaries. Platform and category `Guidance.md` files own listing craft and pricing outputs. Seller profiles own voice, preferences, and approved examples only, because setup never overwrites them and any policy placed there would freeze in every installed workspace.

New-listing works from one seller message containing notes and attached photos: it creates the record, saves the photos beside `Listing.md`, and only then loads the drafting material (guidance, seller profile, category guidance). When no photos are attached it creates the record and asks for them before drafting. Update-listing loads none of this; a bundled script resolves the listing, validates the transition, writes the tracked properties, and moves the folder in one call, because the operation is mechanical and model deliberation only added latency.
## Listing records
Every template shares the same YAML properties: `type`, `platform`, `created`, `posted_price`, `posted_date`, `sold_price`, `sold_date`. The lifecycle folder supplies status, the item folder supplies the display name, and the Base derives time to sell. The body separates seller intake, platform-ready fields, and research notes. Field headings come from each template, so the templates are the field specification.
## Shared and divergent behavior
Facebook Marketplace and eBay share workspace setup, lifecycle folders, common listing properties, co-located photos, the live Base dashboard, and posted/sold tracking. They diverge in platform fields, seller voice, and templates. eBay category folders contain category guidance and a complete template only when the listing form materially differs from the general eBay fallback. The stamp guide asks the seller for specialist facts but does not attempt to become a general collectibles database.
## Host naming
One provider-neutral skill source carries two labels because the hosts derive them differently. Claude labels a plugin skill from its directory name and shows it as `<plugin>:<skill>`, dropping the plugin segment in some surfaces; Codex labels it from `agents/openai.yaml`. A bare `setup` therefore reads as anonymous in Claude while reading correctly in Codex.

Skill directories carry the `marketplace-` prefix so the Claude-side label is self-describing and the three skills group together, and each `agents/openai.yaml` carries the title-case `Marketplace: ...` display name that Codex shows. The directory name remains the single skill identity in both hosts; the Codex adapter is a label, not a second identity. Validation asserts that each adapter declares a display name and references its own skill id, so the two labels cannot drift apart silently.

## Release versioning
The marketplace entry in `.claude-plugin/marketplace.json` repeats the plugin's `plugin.json` version, so releasing the plugin changes the marketplace manifest itself. A manifest that is byte-identical across releases gives a host refresh nothing to detect, and the host keeps offering the installed version. The Codex manifest carries `+codex.<timestamp>` build metadata, which already changes every release.

`plugin.json` wins at install time; the repeated entry version exists to make the change visible. `claude plugin tag` refuses to tag when the two disagree, and repository validation asserts the same agreement so drift is caught before release.

## Deliberate exclusions
- One listing is not cross-posted across platforms.
- The system does not preserve original photos; working copies sit beside `Listing.md`.
- V1 does not track fees, shipping cost, net proceeds, or a price-history ledger.
- The agent does not post listings, contact buyers, or commit to prices without separate authorization.
- The workspace requires Obsidian with the Bases core plugin. It has no dependency on Dataview, Agentic Work, AI Context Handoff, or private vault infrastructure.
