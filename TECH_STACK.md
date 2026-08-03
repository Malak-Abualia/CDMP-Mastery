# Technology Stack

## Purpose

Every technology decision `question_bank/architecture.md` and `quiz_engine/architecture.md` explicitly deferred ("no file format, database engine, or programming language is chosen yet") is resolved here, against the concrete component boundaries in `SYSTEM_ARCHITECTURE.md` and the concrete entities in `DOMAIN_MODEL.md`. Each recommendation states the alternative considered and why it lost, not just the winner — a stack choice without a rejected alternative is not a justified decision.

---

## Language and Runtime: Python 3.12+ (backend/engine/CLI), TypeScript (web only)

**Why Python, not a rewrite in another language:** `quiz_engine/src/quiz_engine/` already exists as a working, tested Python package (33 passing tests, `pyproject.toml`, editable install). Rewriting the Engine Core in a different language to chase a hypothetical performance requirement this single-learner project doesn't have would throw away real, working, tested code for no measurable benefit — the correct move is to build forward from it, not around it. Python's data-science-adjacent ecosystem also matters later for `question_bank/roadmap.md` Phase 3 (Adaptive Questions) if any statistical/ML tooling is ever justified.

**Why TypeScript for the web app specifically:** Next.js (below) is a Node/TypeScript framework; there is no reasonable competing choice here once Next.js is chosen. The web app talks to the Python backend exclusively over HTTP (`SYSTEM_ARCHITECTURE.md`'s dependency graph), so this is a genuine polyglot boundary, not an inconsistency — the web app is a thin client, and thin clients are allowed to be written in whatever language fits their medium best.

---

## Content Schema: Pydantic v2

**Recommendation:** Define `cdmp_content_schema` as a Pydantic v2 package — one model per entity in `DOMAIN_MODEL.md`'s Content Entities section, field-for-field matching `question_bank/metadata_schema.md`'s Field Reference table, using a **discriminated union** on `question_type` for `answer_choices`/`correct_answer` (the polymorphic-shape rationale `DOMAIN_MODEL.md` already justified).

**Why Pydantic over the existing hand-rolled `@dataclass` models** (`quiz_engine/src/quiz_engine/models/question.py`, `results.py`): the current dataclasses correctly define shape but validate nothing — construction happens in `loader/yaml_loader.py` with ad hoc checks. Pydantic collapses "define the shape" and "validate the shape" into one declaration, which matters specifically because `metadata_schema.md`'s enum-constrained fields (`difficulty`, `blooms_level`, `question_type`, `review_status`, `approval_status`, `source_confidence`) and required-field rules are exactly what `quiz_engine/data_loading.md`'s Schema Validation step must enforce on every ingestion run. One Pydantic model, reused by ingestion (validation), the Engine Core (in-memory representation), and FastAPI (request/response schemas — FastAPI is Pydantic-native), removes the class of bug where three hand-written shapes silently drift apart. This is a direct, low-risk migration from the existing dataclasses, not a redesign of the field set.

**Alternative considered — marshmallow / attrs + manual validation:** rejected because neither integrates natively with FastAPI's request/response typing the way Pydantic does, which would reintroduce exactly the "three copies of the same shape" problem this choice exists to eliminate.

---

## Database: PostgreSQL 16+

**Recommendation:** PostgreSQL as the single runtime store for both the `content` schema (ingested from YAML/Markdown) and the `runtime` schema (sessions, attempts, progress), per `SYSTEM_ARCHITECTURE.md`'s Data Flow.

**Why PostgreSQL over SQLite** (the natural lighter-weight alternative for a single-learner project, and worth taking seriously rather than dismissing): three things tip this in Postgres's favor specifically because of decisions already made elsewhere in this design, not as a default enterprise reflex:
1. **Concurrent multi-interface access is a real, near-term requirement, not speculative.** `SYSTEM_ARCHITECTURE.md`'s Concurrency section establishes that a CLI session and a future API/web session can run against the same data at the same time once the API and web app exist (`IMPLEMENTATION_PLAN.md` Sprints 6–8). SQLite's single-writer model is workable for CLI-only use but becomes a real constraint the moment FastAPI is a long-running, potentially concurrent-request server.
2. **JSONB is the correct storage type for the polymorphic fields `DOMAIN_MODEL.md` identified** (`answer_choices`, `correct_answer`, `filters`, `criteria_scores`) — SQLite's JSON support is functional but secondary/text-based; Postgres's JSONB is indexable, queryable, and the de facto standard for exactly this "structured but shape-varies" pattern.
3. **Migration/backup maturity compounds as content grows.** `question_bank/roadmap.md`'s Phase 1 growth targets and eventual Phase 5 (community contributions, however distant) both assume a database that can be backed up, migrated, and restored with standard, well-understood tooling (`pg_dump`, Alembic) rather than a single file that must be handled carefully to avoid corruption under concurrent access.

**Alternative considered — SQLite:** genuinely reasonable for the CLI-only phase of this project and worth revisiting if the project ever needs to run fully offline/embedded with zero infrastructure. Rejected as the long-term choice specifically because the API and web app are explicit, near-term goals in this same document set, not hypothetical future scope.

---

## ORM / Data Access: SQLAlchemy 2.0 (async) + Alembic

**Recommendation:** SQLAlchemy 2.0's async engine for the repository layer (`cdmp_engine.repository`, per `SYSTEM_ARCHITECTURE.md`'s package boundaries — the *only* code permitted to issue SQL), with Alembic for schema migrations, versioning the `content` and `runtime` schemas independently (content-schema migrations track `metadata_schema.md` changes; runtime-schema migrations track scoring/session model changes — the two evolve on different cadences and gating one on the other would be an artificial coupling).

**Why an ORM at all, rather than raw SQL:** the relationships in `DOMAIN_MODEL.md` (self-referential `Question` versioning, many-to-many `Question`↔`KnowledgeArea`, the `Attempt`→`Question` reference that must *not* cascade-delete) are exactly the kind of relational integrity logic that's easy to get subtly wrong by hand and easy to express declaratively in an ORM's model layer, where it's reviewed once rather than re-verified in every hand-written query.

**Why async specifically:** FastAPI's main advantage is native async request handling; a synchronous SQLAlchemy engine underneath it would silently block the event loop on every database call, discarding that advantage. This matters even at single-learner scale because the AI Tutor integration (Sprint 9) will make outbound HTTP calls to the Claude API from within a request — exactly the kind of I/O-bound operation async is designed to not block on.

**Alternative considered — raw `psycopg` + hand-written SQL:** rejected only because the relational-integrity guarantees above are worth the ORM's learning curve; for a project this size the difference is not dramatic, but SQLAlchemy is the safer default given the self-referential and many-to-many relationships already specified.

---

## API Framework: FastAPI

**Recommendation:** FastAPI for `apps/api`, exposing the Quiz Session contract (`start` / `next-question` / `submit-answer` / `end`) plus progress/readiness read endpoints, per `quiz_engine/architecture.md`'s Future Integration → REST API section.

**Why FastAPI over Flask or Django REST Framework:**
- **Pydantic-native.** Request and response models are the *same* `cdmp_content_schema`/domain-model Pydantic classes the Engine Core already uses — no adapter layer translating between an ORM model, a serializer, and an API schema (the three-copies problem the Pydantic decision above already eliminated at the content layer; FastAPI extends that same elimination to the HTTP boundary).
- **Automatic OpenAPI documentation.** This project has already invested heavily in precise, field-level documentation (`metadata_schema.md`'s Field Reference table, `scoring_engine.md`'s Score Record Shape) — FastAPI generates an interactive, always-in-sync API reference directly from the same Pydantic models, rather than requiring a second, hand-maintained API doc that can drift from the code the way a manually written OpenAPI spec would.
- **Async-first**, consistent with the SQLAlchemy async decision above.

**Alternative considered — Django REST Framework:** rejected as heavier than this project needs (full ORM, admin site, templating engine) when SQLAlchemy already covers persistence and Next.js already covers presentation; DRF's strengths (admin UI, batteries-included auth) solve problems this single-learner project doesn't yet have.

---

## CLI Framework: Typer

**Recommendation:** Typer, replacing the existing `argparse`-based `quiz_engine/src/quiz_engine/cli/main.py`.

**Why Typer over continuing with `argparse`:** the existing CLI is functional but its command surface is currently flat (`python -m quiz_engine --ka ... --difficulty ...`), while `quiz_engine/cli_design.md`'s full specification requires a **subcommand structure** (`quiz start`, `quiz resume`, `progress show`, `progress readiness`) with mode-specific flag validation (e.g., `--ka` must be rejected as an error, not silently ignored, when combined with `--mode exam`). Typer is purpose-built for exactly this shape of nested-subcommand CLI, generates `--help` output from type hints and docstrings automatically, and — because it's built on Click and designed to compose with Pydantic — the same `cdmp_content_schema`/domain models validate CLI input the same way they validate API input, again avoiding a third parallel validation implementation.

**Alternative considered — keep `argparse`:** viable and lower-migration-cost, but `cli_design.md`'s command-family structure (multiple subcommands, each with its own flag set and validation rules) is exactly what `argparse` makes verbose and Typer makes declarative; the existing CLI's flat structure would need substantial restructuring to reach the full spec regardless of library, so this is a good moment to switch.

---

## Web Application: Next.js (App Router) + Tailwind CSS

**Recommendation:** Next.js for `apps/web`, styled with Tailwind CSS, consuming `apps/api` exclusively over HTTP (never importing Python code, per `SYSTEM_ARCHITECTURE.md`'s dependency graph).

**Why Next.js over a plain React SPA or a server-rendered Python template (e.g., Jinja2):**
- A quiz-taking UI is inherently interactive (per-question state, timers for Exam Simulation Mode, immediate-vs-deferred feedback per `quiz_modes.md`) — this needs real client-side interactivity, ruling out a server-rendered template approach.
- A progress/readiness dashboard (`UserProgress`, `WeakArea`, `KAScore` trends) benefits from server-side rendering for fast initial load of read-heavy data, which a plain client-only SPA (e.g., bare Vite+React) doesn't give you without extra plumbing Next.js provides out of the box.
- This keeps the web app a strict presentation layer, per `quiz_engine/architecture.md`'s explicit non-goal ("no new session or scoring logic") — Next.js's API routes are deliberately *not* used for business logic here; every data operation goes to the FastAPI backend, preserving the one-contract-many-clients principle.

**Why Tailwind:** the project's design priority (per `cli_design.md`'s own stated principles, carried forward) is plain, readable, functional presentation over visual polish — Tailwind's utility classes let a small, mostly-solo engineering effort build a consistent, readable UI (question cards, score breakdowns, progress charts) quickly without hand-rolling a CSS architecture or adopting a heavier component library this project's scope doesn't justify.

**Alternative considered — Streamlit/Gradio (Python-native dashboard tools):** attractive for the progress-dashboard half of the web app specifically, and would avoid the polyglot boundary entirely. Rejected as the primary web framework because the quiz-taking experience (per-question interaction, timed sessions, immediate feedback rendering) is a poor fit for these tools' page-rerun execution model; Next.js handles both halves (dashboard and interactive quiz) under one framework instead of stitching two different tools together.

---

## AI Tutor Integration: Anthropic Claude API (Messages API)

**Recommendation:** The AI Tutor augmentation (`SYSTEM_ARCHITECTURE.md`'s Augmentation layer) calls the Claude API's Messages endpoint directly from the Feedback stage handoff point, using the current Claude model family available at implementation time.

**Why this, and why it must be called with strict grounding, not general chat:** `quiz_engine/feedback_system.md`'s handoff contract requires every Tutor response to be traceable to the feedback payload's own `dama_concept`/`industry_practice_concept` (tag intact) and `references` — this is implemented as a system-prompt constraint plus the payload passed as explicit context, not as a general-purpose chat interface bolted onto the feedback screen. This is a prompt-engineering and integration-testing concern (verified in Sprint 9, `IMPLEMENTATION_PLAN.md`), not a different model choice — any sufficiently instructable LLM API could technically fill this role; Claude is recommended because it is the assistant already producing this project's content and review work (`CLAUDE.md`), so grounding conventions (`[DAMA]`/`[Industry Practice]` tagging discipline) are already the same vocabulary on both sides of the integration.

---

## Testing

| Layer | Tool | Rationale |
|---|---|---|
| Engine Core, Content Schema | `pytest` (+ `pytest-asyncio` for async repository code) | Already in use (`quiz_engine/tests/`, 33 passing tests) — extend the existing suite rather than replacing the framework |
| API contract | FastAPI's built-in `TestClient` (`httpx`-based) | Exercises real request/response cycles against the same Pydantic schemas the API declares, catching drift between documented and actual behavior |
| Content ingestion | A dedicated integration test mirroring the existing `tests/test_real_question_bank.py` pattern, now asserting against the real, current counts (266 questions, 140 Published/126 Draft, 14 KAs) rather than the superseded Phase-1 figures | Preserves the existing "fires if real content and code drift apart" regression signal `quiz_engine/README.md` already established as a design value |
| Web app | Vitest (unit/component) + Playwright (end-to-end quiz-taking flow) | Standard, well-supported pairing for a Next.js app; Playwright specifically matters for verifying the timed Exam Simulation UI behaves correctly under real browser conditions |

---

## Containerization: Docker + Docker Compose

**Recommendation:** A `docker-compose.yml` providing a local PostgreSQL instance and the FastAPI app, for development; the CLI and web app run natively against that compose stack rather than being containerized themselves during development.

**Why Docker, given this is a single-learner project without a scale requirement:** the justification here is *not* performance or scale — it's eliminating "works on my machine" drift between the environment the Content Ingestion pipeline validates against and the environment `quiz_engine/data_loading.md`'s validation rules are specified against, and giving the eventual CI pipeline (below) an identical database to test against as local development uses. This is a modest, not an enterprise-scale, use of Docker: one Postgres service and one API service, no orchestration platform.

**Alternative considered — a bare local Postgres install (Homebrew/apt/native Windows installer):** works fine for solo local development but doesn't give CI an identical, disposable environment to run ingestion/integration tests against — Docker Compose solves both with one artifact.

---

## CI/CD: GitHub Actions

**Recommendation:** A GitHub Actions workflow with these gates, in order: lint (`ruff`), type-check (`mypy` or `pyright`), `pytest` (engine + API), an Alembic "migrations apply cleanly to a fresh database" check, and — specifically for any PR touching `question_bank/questions/**` — a **content validation job** that runs the Content Ingestion pipeline's validation step (not the full load) against the changed files.

**Why the content-validation gate is the most important addition here, not a generic nicety:** `question_bank/review_process.md`'s Gate 1 (Technical Review) already defines mechanical checks — wording clarity, format correctness, metadata completeness — that a human reviewer currently performs by hand. Once `cdmp_content_schema`'s Pydantic validation exists, those same mechanical checks can run automatically on every content pull request, catching missing required fields or invalid enum values before a human reviewer's time is spent on them. This does not replace Gate 2 (DAMA Review) or Gate 3 (Approval) — DMBOK2 accuracy and final sign-off remain human judgment calls this design does not attempt to automate — but it makes Gate 1 faster and more reliable, which is a genuine, non-speculative benefit given the project already has 266 question records and growing.

**Deployment:** given this remains a personal-scale project, the recommendation is a single small-instance host (e.g., Fly.io, Render, or a personal VPS) running the Dockerized API + Postgres, with the web app deployed to Vercel (Next.js's natural home, with zero-config integration) — not a Kubernetes cluster or multi-region setup, which would solve problems this project does not have. This can be revisited if and when the project's premise changes (e.g., genuine multi-user community contributions, `question_bank/roadmap.md` Phase 5) — that would be the trigger for reconsidering deployment scale, not before.

---

## Summary Table

| Concern | Choice | Primary reason |
|---|---|---|
| Backend/Engine/CLI language | Python 3.12+ | Builds on existing working `quiz_engine` package |
| Web language | TypeScript | Required by Next.js; isolated behind HTTP boundary |
| Content/domain schema | Pydantic v2 | One schema shared by ingestion, engine, and API |
| Database | PostgreSQL 16+ | JSONB for polymorphic fields; concurrent multi-interface access |
| ORM / migrations | SQLAlchemy 2.0 (async) + Alembic | Models the self-referential and m:n relationships in `DOMAIN_MODEL.md` |
| API framework | FastAPI | Pydantic-native; auto-generated OpenAPI docs |
| CLI framework | Typer | Matches `cli_design.md`'s subcommand structure |
| Web framework | Next.js + Tailwind CSS | Handles both interactive quiz-taking and dashboard rendering |
| AI Tutor | Anthropic Claude Messages API | Same vocabulary/tagging discipline as the rest of the project |
| Testing | pytest, FastAPI TestClient, Vitest, Playwright | Extends the existing 33-test suite; adds layer-appropriate tools only where new layers appear |
| Containerization | Docker + Docker Compose | Environment parity between local dev, CI, and ingestion validation |
| CI/CD | GitHub Actions | Automates Gate 1's mechanical content checks, not just code CI |
| Deployment | Fly.io/Render (API+DB) + Vercel (web) | Personal-project scale, revisited only if the multi-user premise changes |
