# Quiz Engine

**Status:** v0.1 implemented — a working Python CLI (`src/quiz_engine/`), covering random / Knowledge-Area-filtered / difficulty-filtered quizzes, single-answer and multiple-select grading, and per-Knowledge-Area scoring. Full design docs below still govern everything not yet built (Practice/Exam Simulation/Weakness modes, feedback beyond explanation+flashcards+reference, progress persistence, REST API, web app, AI Tutor — see `roadmap.md` for the build sequence). No UI exists; this remains a terminal-only tool.

## What this is

The Quiz Engine is the **delivery layer** that turns the Question Bank's static content into an interactive study experience: assembling a quiz, presenting questions, evaluating answers, scoring performance, delivering feedback, and recording progress. It is the first real *consumer* of `question_bank/` as defined in that system's own architecture (`question_bank/architecture.md`, "Core Architectural Principle") — it reads question content, it never owns or edits it.

This document set specifies *what the engine does and how its pieces fit together*, precisely enough that a future implementation (CLI first, then a Python package, REST API, web application, and AI Tutor integration) can be built against a stable contract rather than improvised per interface.

## Implementation (v0.1)

### What v0.1 covers

The smallest slice of the full design (below) that is genuinely useful today: a read-only Loader, a `Question` model, random/KA-filtered/difficulty-filtered selection, shape-based answer evaluation (single answer + multiple select), and Raw Score / Percentage / Knowledge Area breakdown scoring — run from a terminal via `python -m quiz_engine`. It does **not** yet implement Practice/Exam Simulation/Weakness modes as named concepts, the Difficulty Adjustment or Readiness Indicator scores, progress persistence, or any interface beyond the CLI — see `roadmap.md` for what's next and why it's sequenced that way.

### Install

From the `quiz_engine/` directory:

```
python -m pip install -e .
```

This installs the `quiz_engine` package (from `src/`) in editable mode, including its one runtime dependency (`PyYAML`), and registers `python -m quiz_engine` as a working entry point. For running the test suite too, install `requirements-dev.txt` instead:

```
python -m pip install -r requirements-dev.txt
python -m pip install -e .
```

### Usage

```
python -m quiz_engine --ka data_quality --count 10
```

Because every Phase 1 question currently has `review_status: "Draft"` (`research/question_bank_phase1_validation.md` — none have been through `question_bank/review_process.md`'s Gate 1/2/3 pipeline yet), the engine's default strict mode (Published-only, per `data_loading.md`) will correctly find **zero** questions today. To practice with the current, unreviewed content anyway, pass the explicit, loud opt-in flag:

```
python -m quiz_engine --ka data_quality --count 10 --dev-unreviewed
```

Every question and the session summary will be clearly marked `[DEV/UNREVIEWED CONTENT]` when this flag is used — this is intentional, not a bug to silence (`data_loading.md`, "Lifecycle Filter"). Other options: `--difficulty {Beginner,Intermediate,Advanced,Expert}`, `--questions-path <dir>` (override auto-detection), `--seed <int>` (reproducible selection, mainly for testing). Run `python -m quiz_engine --help` for the full list.

### Source layout

```
quiz_engine/
├── src/quiz_engine/
│   ├── loader/     # discover, parse, validate, and status-filter question_bank YAML (read-only)
│   ├── models/     # Question, AnswerResult, KAScore, ScoreReport
│   ├── engine/     # random / Knowledge-Area / difficulty selection
│   ├── scoring/     # answer evaluation (shape-based) + score aggregation
│   ├── cli/         # argument parsing and the interactive terminal session
│   └── utils/       # exceptions, Knowledge-Area folder<->code mapping, path resolution
├── tests/           # unit tests per package above, plus an integration test against
│                     # the real question_bank/questions/ content
├── pyproject.toml
├── requirements.txt
└── requirements-dev.txt
```

### Testing

```
python -m pytest tests/ -v
```

33 tests, including an integration suite (`tests/test_real_question_bank.py`) that loads the actual `question_bank/questions/` tree (read-only) and asserts it still matches `research/question_bank_phase1_validation.md`'s verified counts (120 questions, 20 per Knowledge Area) — a regression signal that fires if the real content and this code ever drift apart.

## What this is not (this phase)

- Not a full implementation of the design below. v0.1 (above) is deliberately the smallest useful slice; most of `quiz_modes.md`, `feedback_system.md`, `progress_integration.md`, and everything past the CLI in `roadmap.md` remains design-only until a later version.
- Not a UI. The CLI's interaction is plain terminal text per `cli_design.md`'s "no UI" constraint — no rendered screens, no graphical interface.
- Not a modification of `question_bank/`. The engine is designed as a strict read-only consumer of it, exactly as `question_bank/architecture.md` requires.
- Not a scoring authority independent of the real exam. Every scoring and readiness concept here is deliberately anchored to `research/cdmp_exam_overview.md`'s documented exam mechanics, not invented from scratch.

## Governance

This design follows `CLAUDE.md`'s existing operating rules for this project:

- **Source hierarchy** (`CLAUDE.md` §5, `research/source_map.md`): wherever this design makes a CDMP-content claim (exam scoring thresholds, difficulty/Bloom's framing), it cites the existing `research/` or `question_bank/` document that already establishes it, and preserves that document's `[DAMA]` / `[Industry Practice]` tagging rather than restating DAMA content independently.
- **No copyrighted reproduction**: this is a software architecture spec: it references DMBOK2 concepts only through the already-vetted `knowledge_base/` and `question_bank/` layers, never original DMBOK2 text.
- **Read-only relationship to upstream systems**: the engine never modifies `question_bank/questions/`, and — as designed here — only ever *appends* structured results to `progress/`, never rewrites question content or prior history.

## Relationship to the rest of the project

- **`question_bank/`** is the sole content source. Every design decision here defers to `question_bank/architecture.md`, `metadata_schema.md`, `question_lifecycle.md`, and `versioning.md` rather than re-deciding questions those documents already settled (e.g., what "Published" means, how a Multiple Select question's answer is shaped).
- **`research/cdmp_exam_overview.md`** anchors every exam-mechanics decision (timing, scoring thresholds, question count) so the engine's Exam Simulation Mode and readiness indicator are grounded in the real exam, not an approximation.
- **`research/question_bank_audit.md`** and **`research/question_bank_phase1_validation.md`** document the current content's real limitations (6 of 14 Knowledge Areas covered; Multiple Select's exam-representativeness unconfirmed) — this design treats those as active constraints, not footnotes, particularly in `question_selection.md` and `quiz_modes.md`.
- **`progress/`** is the intended home for the engine's output (currently an empty directory in the project structure per `CLAUDE.md`) — `progress_integration.md` proposes the record shapes that will live there.
- **`roadmap/four_month_plan.md`** is the study plan this engine ultimately serves — its weekly quiz/review structure is the real-world usage pattern every mode in `quiz_modes.md` is designed against.

## Document index

| Document | Purpose |
|---|---|
| [`architecture.md`](architecture.md) | The end-to-end system design: Question Bank → Loader → Question Engine → Quiz Session → Scoring → Feedback → Progress Tracking, plus the layered view and future-interface integration points. |
| [`data_loading.md`](data_loading.md) | How the Loader reads, validates, and indexes `question_bank/questions/**/*.yaml`, including how it respects the Question Bank's Published/Draft lifecycle. |
| [`question_selection.md`](question_selection.md) | The selection algorithms behind each quiz mode: filtering, sampling, weighting, and anti-repetition logic. |
| [`scoring_engine.md`](scoring_engine.md) | Raw score, percentage, Knowledge Area score, difficulty adjustment, and the CDMP readiness indicator. |
| [`quiz_modes.md`](quiz_modes.md) | Full specification of the five quiz modes: Practice, Knowledge Area, Difficulty, Exam Simulation, and Weakness. |
| [`answer_evaluation.md`](answer_evaluation.md) | Grading logic for Single Answer, Multiple Select, and Scenario-Based questions. |
| [`feedback_system.md`](feedback_system.md) | What a learner sees after answering: correctness, explanation, related concepts, flashcards, and recommended revision. |
| [`progress_integration.md`](progress_integration.md) | How quiz results update `progress/`, feed a future analytics layer, identify weak areas, and show improvement trends over time. |
| [`cli_design.md`](cli_design.md) | The first realized interface: command structure, interaction flow, and session behavior for a command-line study tool. |
| [`roadmap.md`](roadmap.md) | The build sequence from this design through CLI, Python package, REST API, web application, and AI Tutor integration. |

## How to read these documents

Read in this order for a full understanding: `architecture.md` → `data_loading.md` → `question_selection.md` → `quiz_modes.md` → `answer_evaluation.md` → `scoring_engine.md` → `feedback_system.md` → `progress_integration.md` → `cli_design.md` → `roadmap.md`. A future implementer building only the CLI can go straight to `architecture.md` → `cli_design.md` and follow the cross-references outward from there.
