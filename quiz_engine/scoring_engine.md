# Quiz Engine — Scoring Engine

## Purpose

Specifies the **Scoring** stage (`architecture.md`): how an individual answer becomes a correct/incorrect judgment, and how a session's answers roll up into the five score types this design requires — Raw Score, Percentage, Knowledge Area Score, Difficulty Adjustment, and a Readiness Indicator.

## Sourcing Note

The Readiness Indicator below is the one place this document makes CDMP-content claims rather than pure software-design claims. Its thresholds are taken directly from `research/cdmp_exam_overview.md`, which is itself sourced `[DAMA-official pages, cross-checked]` — this document does not re-derive or approximate them.

---

## 1. Raw Score

**Definition:** Count of questions answered correctly, out of questions attempted in the session.

**Rule for Multiple Select:** All-or-nothing by default — a Multiple Select question (or an MS-shaped Scenario-Based question, per `answer_evaluation.md`) counts as correct only if the learner's selected set exactly matches `correct_answer`. This mirrors how these questions were authored (a single canonical correct set, per `question_bank/authoring_guidelines.md`) and how the real exam almost certainly scores multi-part answers if it uses them at all (unconfirmed — see `question_bank/architecture.md`'s open item on this).

**Configurable exception:** Practice Mode only (`quiz_modes.md`) may optionally show *partial-credit* feedback (e.g., "3 of 4 correct options selected, 1 incorrect option also selected") for learning purposes, without changing how Raw Score itself is counted — the count is always all-or-nothing; partial credit is a feedback-only detail (`feedback_system.md`), never a scoring rule. Exam Simulation Mode never shows or implies partial credit, to avoid miscalibrating a learner's sense of real exam performance.

## 2. Percentage

**Definition:** `Raw Score / Questions Attempted × 100`, rounded to the nearest whole percentage point for display, matching how `research/cdmp_exam_overview.md` describes the real exam's own pass thresholds (60% / 70% / 80%, all whole numbers).

## 3. Knowledge Area Score

**Definition:** Percentage, computed identically to §2 but scoped to each Knowledge Area represented in the session, so a learner sees performance broken out per KA, not just overall. This is the data `progress_integration.md`'s weak-area detection and `question_selection.md`'s Weakness Mode both depend on — it must be computed and persisted per session, not only displayed and discarded.

**Minimum sample size for display:** A Knowledge Area score computed from only 1–2 questions is not meaningful (a single lucky or unlucky answer swings it from 0% to 100%). The engine should flag low-confidence KA scores (below a small configurable question count, e.g., fewer than 4 questions from that KA in the session) as low-confidence rather than presenting them with the same weight as a well-sampled KA score.

## 4. Difficulty Adjustment

**Definition:** A difficulty-weighted score, distinct from the unweighted Percentage, that gives more credit for correctly answering harder questions and less for correctly answering easier ones — intended as a *supplementary* signal for calibrating true mastery, not a replacement for the plain Percentage a learner sees as their primary result.

**Method:** Each answered question contributes a weight based on its `difficulty` field (`question_bank/difficulty_framework.md`):

| Difficulty | Suggested weight |
|---|---|
| Beginner | 1.0 |
| Intermediate | 1.5 |
| Advanced | 2.0 |
| Expert | 2.5 (reserved — no Expert-tier content exists yet per `research/question_bank_audit.md`) |

Difficulty-Adjusted Score = `(sum of weights of correctly-answered questions) / (sum of weights of all attempted questions) × 100`.

**Why this matters, concretely:** two learners each scoring 70% raw could be in very different places — one got there missing mostly Beginner questions (a real gap), the other missing mostly Advanced ones (likely closer to Practitioner-ready than the raw percentage alone suggests). The Difficulty Adjustment surfaces this distinction; the plain Percentage alone cannot. These weights are an engine design choice, not a DAMA or exam-official figure — tag internally as an engine convention, not sourced content, and revisit them once real usage data exists.

## 5. Readiness Indicator

**Definition:** Maps a learner's recent performance to the real CDMP Data Management Fundamentals exam's own scoring bands, so "how am I doing" has a concrete, exam-anchored answer rather than an arbitrary label.

**Source of the thresholds** (`research/cdmp_exam_overview.md`, §1): the same DMF exam is scored at three thresholds depending on target certification level:

| Threshold | Certification level |
|---|---|
| ≥ 60% | Associate |
| ≥ 70% | Practitioner (also requires 2 Specialist exams, not assessed by this engine) |
| ≥ 80% | Master (also requires experience/CV, not assessed by this engine) |

**Readiness bands this engine reports**, derived directly from the above:

| Recent performance (Percentage, ideally Difficulty-Adjusted where available) | Reported readiness |
|---|---|
| Below 60% | **Not yet Associate-ready** — foundational gaps remain |
| 60%–69% | **Associate-ready** — would likely clear the Associate threshold today |
| 70%–79% | **Practitioner-level scoring** — matches this project's stated goal (`CLAUDE.md`, "My Goals": push toward Practitioner-level scoring on the Fundamentals exam) |
| 80% and above | **Master-level scoring** on the Fundamentals content itself (Master certification's other requirements — experience, CV — are outside this engine's scope entirely) |

**Critical caveat, must always be surfaced alongside the indicator, not buried:** this readiness signal is only as representative as the question pool it's computed from. Per `research/question_bank_audit.md` §10, the current bank covers 6 of 14 Knowledge Areas and its Multiple Select question type's exam-representativeness is unconfirmed — so today's Readiness Indicator should be labeled **provisional / partial-coverage** until Knowledge Area breadth grows (`question_bank/roadmap.md`) and the Multiple Select question decision is resolved. A learner should never be told "you are Practitioner-ready" based on 6 of 14 Knowledge Areas without that caveat attached in the same breath.

**Recency weighting:** the Readiness Indicator should weight recent sessions more heavily than old ones (a learner's true current level, not a lifetime average) — exact recency-weighting mechanics are an implementation detail deferred to build time; the requirement here is only that "recent" outweighs "old," not a specific decay function.

---

## Score Record Shape (conceptual)

Every session produces one score record with, at minimum: `raw_score`, `questions_attempted`, `percentage`, `knowledge_area_scores` (map of KA → percentage + confidence flag), `difficulty_adjusted_score`, `readiness_band`, and `coverage_caveat` (whether partial-KA-coverage applies). This record is what `feedback_system.md`'s end-of-session summary renders and what `progress_integration.md` persists — defined once here so both documents reference the same shape rather than each inventing their own.

## Non-Goals of This Document

- No statistical/psychometric model (e.g., Item Response Theory) is specified — the difficulty weights above are a simple, transparent heuristic, deliberately not a black-box model, appropriate for this project's current scale and single-learner context.
- No numeric implementation (data types, rounding library, etc.) is specified.
