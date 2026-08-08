# Sources

This directory is the intake point for authoritative CDMP/DMBOK2 references — where they come from, how they're tracked, and what's allowed to live here. It exists so that `knowledge_base/` content can be traced back to a specific, citable source rather than reconstructed from memory.

**Full mapping strategy, priority rules, and conflict resolution live in [`research/source_map.md`](../research/source_map.md). This README covers what belongs in each folder below, the private/public split, and how sources get registered.**

## Hard rule: no copyrighted content

**Never store verbatim DMBOK2 text, scanned/copied pages, PDFs of the book, or any other copyrighted material anywhere in this repo — not in `sources/`, `knowledge_base/`, `research/`, or `question_bank/`.** Tracked repository files may only hold:

- **Citations** — chapter/section/page references (e.g., "DMBOK2 2nd Ed., Ch.3, p.63") pointing to material you own or have legitimate access to elsewhere.
- **Paraphrased summaries** — your own words, synthesizing a concept, always tagged per the `[DAMA]` / `[Industry Practice]` / `[Regulation/Standard]` convention in `research/source_map.md`.
- **Links** — to official DAMA pages, public regulatory texts, and freely-licensed standards documentation.
- **Metadata** — bibliographic detail in `research/source_registry.yaml` (title, author, edition, etc. — never the work's actual content).

Short (<25 word) quoted fragments used for direct definitional precision are acceptable if clearly marked as a quote with a citation. Anything longer gets paraphrased.

## Private resources vs. public source metadata

Every source falls into one of two zones. This is a hard boundary, not a style preference:

| | Private (local-only) | Public source metadata (committed) |
|---|---|---|
| **What it is** | The actual copyrighted file itself — a PDF, ebook, scanned pages, licensed prep-vendor content | Citations, bibliographic metadata, links, and your own paraphrased notes *about* that file |
| **Where it lives** | The relevant `sources/<folder>/` directory, as a file sitting alongside that folder's `README.md` (e.g. `sources/dmbok2/dama-dmbok-2nd-edition-data-management.pdf`) | `research/source_registry.yaml` (one entry per source) + short pointer notes in `sources/<folder>/README.md` |
| **Git status** | **Must be git-ignored.** Covered today by the `sources/dmbok2/*.pdf` (and sibling ebook-format) rules in the root `.gitignore`. If you add another private full-text file under a different `sources/` subfolder, add a matching `.gitignore` rule for it *before* it's ever staged. | Tracked normally — this is exactly what's safe and expected to be on GitHub. |
| **Example** | `sources/dmbok2/dama-dmbok-2nd-edition-data-management.pdf` | The `dmbok2-2nd-ed` entry in `research/source_registry.yaml`, plus `sources/dmbok2/README.md` |

**Before adding any new private file:** confirm it's covered by `.gitignore` (`git check-ignore -v <path>`) *before* running `git add`. Never rely on remembering to leave it unstaged.

## How a source gets a `source_id` and gets registered

1. Add the source's metadata as a new entry in [`research/source_registry.yaml`](../research/source_registry.yaml) — one entry per source, with a unique `source_id`.
2. Field definitions and allowed values (including `authority_level` and `classification`) are documented in [`research/source_registry_schema.md`](../research/source_registry_schema.md) — it mirrors the tiers in `research/source_map.md` §5 rather than defining a new hierarchy.
3. If the source has a private local file, place it in the appropriate `sources/<folder>/` directory and confirm `.gitignore` covers it (see table above) before the registry entry is saved.
4. Add a short pointer note in that folder's `README.md` — not a duplicate of the full registry entry, just enough to orient someone browsing the folder.

## How future `knowledge_base/` and `question_bank/` content will reference sources

This is a forward-looking convention, not yet in effect for existing content: once content production resumes, a claim in `knowledge_base/` or a question in `question_bank/` cites a source by its `source_id` (from `research/source_registry.yaml`) plus a locator — e.g. a `[DAMA]`-tagged claim traces to `source_id: dmbok2-2nd-ed` at a specific chapter/section, using that entry's `citation_format`. This keeps every claim traceable to a registered, authority-ranked source instead of an unverifiable memory of the text. It does not retroactively change any already-completed `knowledge_base/` file.

## Folder structure

| Folder | Purpose |
|---|---|
| `dmbok2/` | **Private.** DAMA-DMBOK2, 2nd Edition — the licensed source file itself (git-ignored) plus your own chapter notes and a page/section index (tracked; paraphrase only, never reproductions). |
| `exam_guide/` | Notes on the official CDMP/DMF exam guide (format, scoring, objectives) once located, plus Specialist exam guides when that phase starts. |
| `dama_official/` | Links and notes on official DAMA International resources: dama.org pages, the DAMA Dictionary, chapter webinars. |
| `industry/` | Named regulations, standards, and reputable secondary sources that DMBOK2 itself references or that provide real-world grounding (e.g., BCBS 239, HIPAA, GDPR, ISO 8000). |

Each folder's `README.md` describes what belongs there. Population happens incrementally, source by source, not as a bulk import. `research/source_registry.yaml` is the single index across all four folders — see field docs in `research/source_registry_schema.md`.
