# Question Bank

**Status:** Architecture and documentation only. No questions have been authored yet. No application code exists yet.

## What this is

The Question Bank is the **canonical content repository** for every assessment surface this project will ever build: quiz sessions, timed mock exams, spaced-repetition flashcards, an AI tutor, a CLI study tool, and eventually a web application and REST API. It is not a quiz, and it is not a feature — it is the data layer everything else reads from.

Every other assessment tool in this project is, architecturally, a *consumer* of the Question Bank. None of them are permitted to own question content directly. This separation (content vs. delivery) is the single most important architectural decision in this design — see `architecture.md`, "Core Architectural Principle."

## What this is not (this phase)

- Not a working application. Nothing here executes.
- Not a set of real questions. Every example in these documents is a structural placeholder, not exam content.
- Not a replacement for `knowledge_base/`. The Question Bank *tests* what `knowledge_base/` *teaches* — it does not duplicate explanations, only references them.
- Not a modification of any existing folder. `knowledge_base/`, `research/`, `roadmap/`, `reviews/`, and `sources/` are untouched by this design.

## Relationship to the rest of the project

- **`research/source_map.md`** governs sourcing for the Question Bank exactly as it governs `knowledge_base/`: DAMA-DMBOK2 is primary authority, official DAMA guidance is next, industry practice is illustrative only. Every question must carry the same `[DAMA]` / `[Industry Practice]` distinction used throughout the knowledge base. See `question_quality_standards.md`.
- **`knowledge_base/`** is the source of truth every question must trace back to. A question cannot exist without a named source section in a specific `knowledge_base/*.md` file. See `taxonomy.md`.
- **`CLAUDE.md`**'s Knowledge Base Operating Workflow (module creation → review → improvement → approval) is the direct precedent for this system's own lifecycle. The Question Bank's review process (`review_process.md`) is deliberately parallel to, but distinct from, the module-level review process already in place — see `review_process.md` for how the two relate.
- **`roadmap/four_month_plan.md`** determines which Knowledge Areas have content mature enough to be questioned. A Knowledge Area should generally be an **Approved** `knowledge_base/` module (per `CLAUDE.md`, Approval Workflow) before its Question Bank content is authored — see `authoring_guidelines.md`.

## Document index

| Document | Purpose |
|---|---|
| [`architecture.md`](architecture.md) | The system design: how a question flows from authoring to every consuming surface, the storage model, and integration points with all downstream systems. |
| [`taxonomy.md`](taxonomy.md) | The subject classification structure (Knowledge Area → Topic → Subtopic) every question is filed under, mapped to the existing 14 DMBOK2 Knowledge Areas. |
| [`question_lifecycle.md`](question_lifecycle.md) | The state machine a question moves through, from Draft to Retired, and what's true/allowed at each state. |
| [`question_quality_standards.md`](question_quality_standards.md) | The non-negotiable bar every question must clear before it can be approved. |
| [`authoring_guidelines.md`](authoring_guidelines.md) | The practical, step-by-step guide for writing a new question, including stem/distractor/explanation style rules. |
| [`metadata_schema.md`](metadata_schema.md) | The full field-by-field data schema every question record must satisfy. |
| [`versioning.md`](versioning.md) | How questions change over time without breaking historical analytics or silently mutating published content. |
| [`difficulty_framework.md`](difficulty_framework.md) | The four difficulty levels (Beginner → Expert), what distinguishes them, and how they map to Bloom's Taxonomy and CDMP exam relevance. |
| [`review_process.md`](review_process.md) | The concrete, gated review pipeline (Technical Review + DAMA Review) with pass/fail criteria at each gate. |
| [`naming_conventions.md`](naming_conventions.md) | The Question ID scheme (e.g., `GOV-001`), Knowledge Area codes, and file/path conventions. |
| [`roadmap.md`](roadmap.md) | How this system matures from static knowledge questions through adaptive and AI-generated questions to community contributions. |

## How to read these documents

Read in this order for a full understanding: `architecture.md` → `taxonomy.md` → `metadata_schema.md` → `difficulty_framework.md` → `question_lifecycle.md` → `review_process.md` → `question_quality_standards.md` → `authoring_guidelines.md` → `naming_conventions.md` → `versioning.md` → `roadmap.md`. Each document is also independently referenceable once the system is in use — a question author, for instance, will mostly live in `authoring_guidelines.md`, `metadata_schema.md`, and `naming_conventions.md` day to day.
