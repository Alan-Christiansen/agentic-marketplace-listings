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

Update-listing uses a one-turn fast path when the seller identifies one listing, states the action, and supplies its required values. Its normal transitions are Building to Ready, Building or Ready to Posted, Posted to Sold, and Building, Ready, or Posted to Closed; a current-price change remains in Posted. The agent performs one compact read-only preflight, asks one grouped question only for missing required values, and does not request duplicate confirmation for a complete instruction. Corrections, terminal-state reopening, ambiguous listings, and transitions outside this matrix use an explicit review-and-approval path. Repeating an already-current update is a no-op rather than an error.
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
New-listing uses two stages. In the first stage, the agent loads only the shared operating policy, selected template, workspace markers, and lifecycle folder names needed to create an unambiguous Building record. It then reports the exact item-folder path and pauses for photo export. An explicit statement that there will be no photos bypasses the pause.

After the seller confirms the photos are ready, the agent progressively loads only the remaining information relevant to that listing:
1. The item-specific note and co-located photos.
2. The selected platform guide and seller profile, including that platform's approved prose examples.
3. Category guidance when applicable, beginning with eBay stamps.

Examples demonstrate voice and structure only. Their facts, prices, condition statements, and platform details must never be reused as item evidence.
## Listing records
Every platform and category template retains the shared record type, platform, creation date, posted price and date, and sold price and date as YAML properties. The lifecycle folder supplies status, the item folder supplies the display name, and the Base derives time to sell. The body separates seller-supplied intake information from platform-ready fields and optional research notes. New-listing creates and saves the intake record before photo-dependent preparation begins. Facebook supports free-form notes, features, and dimensions before producing Title, Price, Category, Condition, and Description. The eBay stamp template produces Title, Price, Seller Notes, Place of Origin, Quality, Grade, Country of Origin, Certification, Category, and Item Description. Unknown values remain blank or explicitly unknown rather than being invented.
## Shared and divergent behavior
Facebook Marketplace and eBay share workspace setup, lifecycle folders, common listing properties, co-located photos, the live Base dashboard, and posted/sold tracking. They diverge in platform fields, seller voice, and templates. eBay category folders contain category guidance and a complete template only when the listing form materially differs from the general eBay fallback. The stamp guide asks the seller for specialist facts but does not attempt to become a general collectibles database.
## Host naming
One provider-neutral skill source carries two labels because the hosts derive them differently. Claude labels a plugin skill from its directory name and shows it as `<plugin>:<skill>`, dropping the plugin segment in some surfaces; Codex labels it from `agents/openai.yaml`. A bare `setup` therefore reads as anonymous in Claude while reading correctly in Codex.

Skill directories carry the `marketplace-` prefix so the Claude-side label is self-describing and the three skills group together, and each `agents/openai.yaml` carries the title-case `Marketplace: ...` display name that Codex shows. The directory name remains the single skill identity in both hosts; the Codex adapter is a label, not a second identity. Validation asserts that each adapter declares a display name and references its own skill id, so the two labels cannot drift apart silently.

## Deliberate exclusions
- One listing is not cross-posted across platforms.
- The system does not preserve original photos; working copies sit beside `Listing.md`.
- V1 does not track fees, shipping cost, net proceeds, or a price-history ledger.
- The agent does not post listings, contact buyers, or commit to prices without separate authorization.
- The workspace requires Obsidian with the Bases core plugin. It has no dependency on Dataview, Agentic Work, AI Context Handoff, or private vault infrastructure.
