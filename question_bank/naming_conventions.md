# Question Bank — Naming Conventions

## Purpose

Defines the Question ID scheme, the Knowledge Area code table, and the conceptual file/path naming pattern the system will use once implementation begins.

## Question ID Format

```
<KA_CODE>-<sequence>
```

- `KA_CODE` — a fixed abbreviation for one of the 14 Knowledge Areas (table below).
- `sequence` — a zero-padded, three-digit, strictly incrementing number, unique within that Knowledge Area, starting at `001`.

**Examples (format only — none of these IDs are assigned to real content):** `GOV-001`, `QUAL-015`, `META-021`, `ARCH-008`, `MODEL-013`, `MASTER-004`.

## Why the ID Excludes the Version

The Question ID is a **permanent identity**; the version (`versioning.md`) is a **mutable attribute** of that identity. `GOV-001` refers to the same question across its entire lifetime, from `v1.0` through however many major revisions it accumulates — the ID never encodes `v1`, `v2`, etc. This is what allows `metadata_schema.md`'s `supersedes`/`superseded_by` links and Analytics' historical tracking (`versioning.md`) to work: a response logged against "`GOV-001`, version `1.0`" stays meaningful even after `GOV-001` reaches version `2.0`, because the ID that ties it all together never changed.

## Sequence Rules

- Sequence numbers are assigned strictly in authoring order within a Knowledge Area — the next new GOV question is always `GOV-<highest existing + 1>`, regardless of topic or difficulty.
- A sequence number is **never reused**, even after a question is permanently Retired (`question_lifecycle.md`). `GOV-001`, once retired with no successor, stays retired forever — the number is not recycled for an unrelated new question, to prevent any possibility of an old analytics record being misread as referring to new content.
- Gaps in the sequence are acceptable and expected over time (e.g., after a terminal retirement) and carry no special meaning.
- Three digits (`001`–`999`) is the starting allocation per Knowledge Area; if a Knowledge Area's question count ever approaches 999 (not anticipated at this project's scale), the format would extend to four digits — a decision deferred until it's an actual constraint, not a hypothetical one.

## Knowledge Area Code Table

| Code | Knowledge Area |
|---|---|
| GOV | Data Governance |
| ARCH | Data Architecture |
| MODEL | Data Modeling and Design |
| STOR | Data Storage and Operations |
| SEC | Data Security |
| INTEG | Data Integration and Interoperability |
| DOC | Document and Content Management |
| MASTER | Reference and Master Data |
| DWBI | Data Warehousing and Business Intelligence |
| META | Metadata Management |
| QUAL | Data Quality |
| BIGDATA | Big Data and Data Science |
| MAT | Data Management Maturity Assessment |
| ETH | Data Ethics |

This table must stay identical to `taxonomy.md`'s Knowledge Area Index — if they ever diverge, this document governs the ID format and `taxonomy.md` governs content scope, but divergence itself should be treated as a defect to fix immediately, not a tolerated inconsistency.

## Conceptual File / Path Naming (not created in this phase)

When implementation begins, the intended convention (see `architecture.md`, "Storage Model") is:

```
question_bank/questions/<KA_CODE>/<QUESTION_ID>.yaml
```

e.g., `question_bank/questions/GOV/GOV-001.yaml`. One file per question, grouped into one directory per Knowledge Area — directly extending the naming logic already used by `knowledge_base/` (one file per Knowledge Area) down to the individual-question level, since a Knowledge Area will eventually hold many question records rather than one module document.

## Forward-Looking Convention: Question-Level Reviews

If a future review pass ever needs to record findings against an individual question (distinct from the Gate 1–3 pass/fail checklist already tracked on the question record itself, per `review_process.md`), the naming pattern should follow the precedent already established for module-level reviews (`reviews/<module_name>_review.md`):

```
reviews/questions/<QUESTION_ID>_review.md
```

e.g., `reviews/questions/GOV-001_review.md`. This is documented here for consistency but is not required by the standard Gate 1–3 process, which tracks review history directly on the question record (`review_status`, `reviewer`) rather than in a separate file — a separate review file would only be warranted for an unusually contested or complex question requiring extended documentation.

## Other Naming Rules

- **Knowledge Area codes are fixed and never change** once assigned, even if the Knowledge Area's display name is later revised — a code change would break every existing Question ID referencing it.
- **Codes are always uppercase**, questions IDs always follow the exact `KA-###` pattern with a single hyphen — no lowercase, no underscores, no additional separators, so that ID parsing (by any future tooling) can rely on a single, simple, unambiguous format.
