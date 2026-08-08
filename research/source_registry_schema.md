# Source Registry Schema

Defines every field in `research/source_registry.yaml` and its allowed values. This is documentation only — it does not itself register any source and does not change the authority hierarchy defined in `research/source_map.md` §5.

## Purpose

`source_registry.yaml` is a metadata index: one entry per reference source used anywhere in this project (DMBOK2, the DAMA Dictionary, the CDMP exam guide, named regulations, prep-provider material, etc.). It exists so that, once content production resumes, `knowledge_base/` and `question_bank/` content can cite a `source_id` instead of re-describing a source inline every time — and so every source's authority tier and copyright status is recorded in exactly one place.

**A registry entry never contains the source's copyrighted content itself** — only bibliographic metadata, a citation format, and project-authored notes.

## Fields

| Field | Required | Type | Description |
|---|---|---|---|
| `source_id` | Yes | string | Unique, stable, kebab-case identifier. Never renamed once referenced elsewhere (future `knowledge_base/`/`question_bank/` citations will point to it). Convention: `<short-name>-<version-or-qualifier>`, e.g. `dmbok2-2nd-ed`, `dama-dictionary`, `cdmp-exam-info-pricing`. |
| `title` | Yes | string | Full title of the work, page, or document. |
| `author` | No | string or `null` | Individual author(s) if credited. `null` when the work is organization-authored (e.g. DMBOK2 is credited to DAMA International as a body, not a named individual). |
| `organization` | Yes | string | Publishing or issuing organization (e.g. `DAMA International`, `HHS` for HIPAA, a named prep-vendor). |
| `source_type` | Yes | enum | One of: `book`, `dictionary`, `exam_guide`, `website`, `regulation`, `standard`, `prep_provider_material`, `webinar`, `blog_article`, `other`. |
| `authority_level` | Yes | integer 1–6 | Maps directly to the priority tiers in `research/source_map.md` §5 (1 = highest authority). See table below. Determines which source wins when two disagree. |
| `classification` | Yes | enum | One of: `private_copyrighted`, `public_link`, `public_standard`. See below. |
| `version` | No | string or `null` | Edition, revision, or version identifier (e.g. `"2nd Edition"`). `null` if not applicable/not yet confirmed — never guessed. |
| `publication_date` | No | string or `null` | ISO date or year, only if confirmed from the source itself or existing project docs. `null` if unconfirmed — do not invent a date. |
| `url` | No | string or `null` | Public URL. Required (non-null) when `classification` is `public_link` or `public_standard`. `null` for `private_copyrighted` sources with no accompanying public page. |
| `local_private_path` | No | string or `null` | Repo-relative path to a locally held private file. Required (non-null) when `classification` is `private_copyrighted`. That path (or its containing directory) **must** have a matching rule in the root `.gitignore`. |
| `citation_format` | Yes | string | The template used when this source is cited in `knowledge_base/` or `question_bank/` content, e.g. `"DMBOK2 2nd Ed., Ch.<N> <Chapter Name>, §<section>"`. |
| `copyright_status` | Yes | string | Free-text statement of copyright/usage constraints: whether the work is copyrighted, the basis on which it's held (e.g. personal legally obtained copy), and what is/isn't allowed to be reproduced from it in this repo. |
| `notes` | No | string | Provenance, open questions (unconfirmed edition/errata, etc.), or other context. Mirror open items into `research/source_map.md` / `research/cdmp_exam_overview.md` rather than letting them live only here. |

## `authority_level` values

Directly mirrors `research/source_map.md` §5 — do not maintain a second hierarchy here.

| Level | Tier |
|---|---|
| 1 | DAMA-DMBOK2 (2nd Edition) |
| 2 | Official DAMA/CDMP exam guide + dama.org pages |
| 3 | DAMA Dictionary of Data Management Terminology |
| 4 | Named regulations/standards (BCBS 239, HIPAA, GDPR, ISO 8000, etc.) |
| 5 | Reputable CDMP prep-provider material |
| 6 | General industry blogs/practitioner content |

## `classification` values

| Value | Meaning | Constraints |
|---|---|---|
| `private_copyrighted` | Full-text copyrighted work held locally only (e.g. the DMBOK2 PDF). Never committed. | `local_private_path` required; that path must be covered by `.gitignore`; only paraphrase/short-quote (<25 words, marked) may appear in tracked files, per `sources/README.md`. |
| `public_link` | Freely accessible official page/resource (dama.org pages, an official exam guide posted publicly). Safe to link. | `url` required. The repo stores a link + short note, not a mirror of the page content. |
| `public_standard` | Publicly available regulation or standard (HIPAA, GDPR, ISO 8000 text/summaries). Citable, brief quotation permitted with attribution. | `url` required if a canonical public copy exists; otherwise cite by name and issuing body. |

## Adding a new source

1. Append a new entry to `research/source_registry.yaml` with a new, never-reused `source_id`.
2. If `classification: private_copyrighted`, confirm the local file's directory is covered by `.gitignore` before saving the entry — do not register a private source that isn't yet ignored.
3. Add a short pointer note (not a duplicate of the registry entry) in the relevant `sources/<folder>/README.md` per the existing structure in `sources/README.md`.
4. Do not invent `version`, `publication_date`, `author`, or other factual fields that can't be verified from the file itself or existing project documentation — use `null` and log the gap in `notes` instead.

## How future content will reference a source

Once content production resumes, a `knowledge_base/` or `question_bank/` entry cites a source by its `source_id` plus a locator (chapter/section/page, per that source's `citation_format`) rather than re-typing bibliographic detail inline — e.g. a claim tagged `[DAMA]` traces back to `source_id: dmbok2-2nd-ed` at a specific `§`. This is a forward-looking convention only: it does not retroactively change any existing `knowledge_base/` file, which is out of scope for this source-intake task.
