# Question Bank — Versioning

## Purpose

Questions change over time — a typo is found, analytics reveals a bad distractor, a `knowledge_base/` module is revised, DMBOK2 guidance is clarified. This document defines how change happens **without** silently mutating what a learner already saw, and without corrupting historical analytics that reference a specific question by ID.

## Core Principle: Published Content Is Never Silently Edited

Once a question reaches `Published` (`question_lifecycle.md`), its content and metadata are immutable at that version. Any change creates a new version. This mirrors the same principle already established for `knowledge_base/` modules under `CLAUDE.md`'s Approval Workflow: *"Treat an Approved module as stable... fix it deliberately and note the change, never edit... silently."* The Question Bank applies this at the level of a single question rather than a whole module.

## Version Format: `MAJOR.MINOR`

- Every question starts at **`1.0`** the moment it first reaches Published.
- **MINOR** increments (`1.0` → `1.1`) are for non-substantive edits: typo fixes, formatting cleanup, a metadata field correction that doesn't change meaning (e.g., adding a missing `keyword`). A minor version bump does **not** require re-entering the full review pipeline — a lightweight Technical Review check is sufficient, since nothing DAMA-substantive changed.
- **MAJOR** increments (`1.x` → `2.0`) are for substantive edits: the stem is reworded in a way that could change interpretation, an answer option is added/removed/changed, the correct answer changes, or the explanation's reasoning is materially revised. A major version bump **must** re-enter the full pipeline (Draft → Technical Review → DAMA Review → Approval) exactly as if it were a new question, because its correctness has not yet been re-verified.

## What Triggers a New Version

| Trigger | Version type | Source |
|---|---|---|
| Typo, formatting, or non-substantive metadata fix | Minor | Author or reviewer notices during unrelated work |
| Analytics flags an anomalous miss rate or unused distractor | Major (usually) | Analytics Engine → Revision Trigger (`architecture.md`) |
| A `knowledge_base/` module the question cites is itself revised | Major (if the revision affects the tested fact) or no action (if unaffected) | `CLAUDE.md` Improvement Workflow completing on the source module |
| DAMA Review discovers an error post-publication | Major | Manual discovery |
| The question's Knowledge Area exam weighting changes materially | Re-evaluate for Retirement, not necessarily a new version | `research/cdmp_exam_overview.md` update |

## Supersession Chain

Each question's record carries two system-managed links (defined in `metadata_schema.md`, "Versioning-Related Metadata"):

- `supersedes` — points to the prior version this one replaces, if any.
- `superseded_by` — points to the newer version that replaced this one, once it exists.

When a major version is Published, the **prior version is immediately Retired** (`question_lifecycle.md`) rather than remaining live alongside its replacement — a learner or exam simulation should never be able to draw both `GOV-001 v1.0` and `GOV-001 v2.0` into the same session. The Question ID (`GOV-001`) stays constant across versions; only the `version` field changes. This is why `naming_conventions.md` deliberately keeps the ID and the version as separate concepts — the ID is a permanent identity, the version is a mutable attribute of that identity.

## Why Historical Analytics Survive Versioning

A learner's response to `GOV-001 v1.0` is recorded against that exact version, not just the ID. If `v1.0` is later found to have a flawed distractor and `v2.0` corrects it, the learner's historical `v1.0` response remains a valid, unaltered record of what actually happened — it is not retroactively reinterpreted. Analytics that aggregate "performance on `GOV-001`" across versions must do so explicitly and transparently (e.g., clearly noting a version boundary in a trend chart), never silently. This is a direct consequence of `architecture.md`'s Question State Visibility table: Retired questions remain queryable in Analytics precisely so this kind of longitudinal integrity is possible.

## Deprecation vs. Retirement vs. Archival

Three distinct outcomes, not synonyms:

- **Superseded** — a specific version is replaced by a newer version of the *same* question (see Supersession Chain above). The old version is marked Retired but its ID lineage continues via `superseded_by`.
- **Retired (terminal)** — the question (all versions) is permanently withdrawn with no replacement planned — e.g., its topic fell out of exam scope. No `superseded_by` link exists.
- **Archival** — not a lifecycle state but a storage-layer property: all Retired questions (superseded or terminal) remain physically present and queryable (`architecture.md`), never deleted. "Archival" simply describes that retired records live in the same durable store as active ones, not a separate cold-storage tier requiring different tooling — this project has no scale requirement yet that would justify that distinction.

## Analytics-Driven Revision (conceptual)

The Analytics Engine (`architecture.md`) is expected to flag a Published question for review when its response data shows a statistically anomalous pattern — for example, a miss rate far outside what its `difficulty` level predicts, or a distractor that's essentially never selected (suggesting it's too implausible to discriminate anything, per `question_quality_standards.md`, Standard 6). This design fixes the *concept* of that feedback loop (shown in `architecture.md`'s End-to-End Flow diagram as the "Revision Trigger") — the actual statistical thresholds and detection logic are an implementation detail deferred to when an Analytics Engine is actually built.
