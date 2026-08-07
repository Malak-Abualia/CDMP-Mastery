# Engineering Architecture Review

> Reviews the Engineering Phase design-document set as a unit: `SYSTEM_ARCHITECTURE.md`, `DOMAIN_MODEL.md`, `TECH_STACK.md`, `IMPLEMENTATION_PLAN.md`. Modeled on the Knowledge Base Review Workflow (`CLAUDE.md`), adapted to engineering-architecture criteria in place of DAMA/CDMP criteria. This review is read-only with respect to the reviewed documents.

## Document Set Information

- **Documents Reviewed:** `SYSTEM_ARCHITECTURE.md`, `DOMAIN_MODEL.md`, `TECH_STACK.md`, `IMPLEMENTATION_PLAN.md`
- **Upstream Specs (consulted for consistency, not reviewed):** `quiz_engine/architecture.md`, `question_bank/architecture.md`
- **Review Date:** 2026-08-03
- **Reviewer:** Claude (Engineering Architecture Review)
- **Iteration:** 2 (post-improvement re-review; iteration 1's findings below are preserved for record)

---

## Overall Quality Score

**Score:** 93 / 100

**Status:**
- [ ] Draft
- [ ] Needs Improvement
- [x] Approved

---

## Evaluation Criteria

### 1. Architecture Quality — 94/100 *(was 88)*

The six-layer component map (`SYSTEM_ARCHITECTURE.md`) is unusually rigorous for a personal project: each layer states its Reads/Writes/Owns columns explicitly, the "why these six layers and not fewer" section pre-empts the obvious collapsing temptation with a concrete argument, and every decision is anchored to a real starting state (266 questions, 33 passing tests) rather than a hypothetical one. The Mermaid data-flow diagrams are consistent with the prose.

**Iteration 1 gaps, now closed:** `SYSTEM_ARCHITECTURE.md` now has a "Cross-Cutting Concerns: Configuration, Observability, Resilience" section naming all three as threaded-through, not owned-by-one-layer, concerns, with each pointed at its `TECH_STACK.md` detail (Configuration and Secrets Management; Observability; the AI Tutor resilience note). The Claude API call's timeout/retry/graceful-degradation behavior is now specified.

Remaining minor note (not score-blocking): the cross-cutting section is appropriately brief given this project's scale — it names the seam rather than fully designing it, which is the right amount of design-time investment for a solo project, but is worth remembering is a starting point, not a finished spec, once implementation begins.

### 2. SOLID Compliance — 92/100 *(was 82)*

- **SRP** is strong and explicit — every package/layer states one reason to change.
- **OCP** is reasonably served by the discriminated-union answer-shape design and the layered dependency graph.
- **DIP** is now concrete, not just asserted: `repository` defines a `Repository` Protocol; `selection`/`scoring`/`evaluation`/`progress` depend on that abstraction, never on `SQLAlchemyRepository` directly (`SYSTEM_ARCHITECTURE.md`'s Package Boundaries section, `TECH_STACK.md`'s Repository Interface section). The top-level and internal dependency rules are both enforced by `import-linter` in CI (`TECH_STACK.md`'s CI/CD section, `IMPLEMENTATION_PLAN.md` Sprint 10), not by code-review discipline alone.
- **ISP** is served by the same `Repository` Protocol being scoped to what Engine Core actually needs, rather than a generic CRUD interface.
- **LSP** is satisfied by construction: `InMemoryRepository` and `SQLAlchemyRepository` are required to be interchangeable behind the same Protocol, and Sprint 2's acceptance criteria now explicitly test that both implementations agree on the same assertions — the substitutability claim is verified, not just structural.

### 3. Package Boundaries — 95/100 *(was 90)*

The physical layout, the strict one-way dependency diagram, and the explicit list of what does *not* import what are all concrete and testable-in-principle. This remains the document set's strongest section.

**Iteration 1 gap, now closed:** the internal `cdmp_engine` sub-package rule is now stated explicitly ("the same rule applies one level down") and enforced by the same `import-linter` configuration as the top-level graph, so `selection/` reaching into `repository/`'s SQLAlchemy session directly is now a CI failure, not an unstated risk.

### 4. Separation of Concerns — 92/100 *(was 85)*

Layer responsibilities are clean and the AI Tutor's "not a peer in the dependency graph, invoked from Feedback with bounded input" framing is a genuinely good enforcement of grounding-by-construction.

**Iteration 1 gap, now closed:** configuration and observability now have a single named owner (`Settings`, the stdlib-logging convention) rather than an implicit expectation that each package invents its own. Error/exception-handling convention remains lightly specified (each layer's own exception types, propagated rather than swallowed, is implied by the layering but never written as an explicit rule) — a minor remaining gap, not a structural one, since Python's exception propagation is the sane default absent a stated reason to do otherwise.

### 5. Scalability — 91/100 *(was 88)*

The Postgres-over-SQLite reasoning in `TECH_STACK.md` is grounded in a real, near-term requirement (concurrent CLI+API+web sessions) rather than a default enterprise reflex, and says so explicitly. The single-learner non-goal is stated honestly rather than papered over.

**Iteration 1 gap, substantially closed:** the `Repository` Protocol introduced for testability is also, incidentally, the correct seam for introducing caching or a read replica later (a second `Repository` implementation, same interface) — this is now a structurally obvious extension point rather than an undiscoverable one, even though the review does not require it to be spelled out further given the explicit non-goal.

### 6. Testability — 96/100 *(was 87)*

This is the document set's best-supported claim, and is now stronger still: `IMPLEMENTATION_PLAN.md`'s acceptance criteria are unusually concrete and falsifiable (e.g., "mutates a Question's classification after an attempt exists and confirms the historical Attempt row is unaffected"), and `TECH_STACK.md`'s testing table assigns a tool per layer with a stated rationale, now split into an explicit unit tier (DB-free, `InMemoryRepository`) and integration tier (real Postgres, proving the fake and the real implementation agree).

**Iteration 1 gap, now closed:** the fast, DB-free unit-testing seam this review flagged as missing is now the `InMemoryRepository`, delivered in Sprint 1 specifically so Sprint 2 onward never needs a live database for Engine Core unit tests.

### 7. Extensibility — 92/100 *(was 86)*

Genuinely good forward-looking seams: `Learner` modeled today for a multi-user future that doesn't exist yet; `WeakArea` status-flipped rather than deleted; independent Alembic migration tracks for `content` vs. `runtime` schemas.

**Iteration 1 gap, now closed:** `DOMAIN_MODEL.md`'s `SourceCitation` section now names the `provenance` seam on `Question` (`Human/AIGenerated/CommunitySubmitted`) anticipating `question_bank/roadmap.md`'s named future phases, explicitly as a seam to extend later rather than a redesign to do now — consistent with this document set's existing discipline of naming a seam without over-designing it prematurely.

### 8. Future AI Integration — 94/100 *(was 84)*

The grounding contract (bounded input from the Feedback stage, a regression suite asserting citation presence, an explicit out-of-scope test case) is well designed and remains the most carefully specified integration in the whole document set.

**Iteration 1 gaps, now closed:** `TECH_STACK.md`'s AI Tutor section and `IMPLEMENTATION_PLAN.md` Sprint 9 now specify timeout + single retry + graceful fallback to a Tutor-less feedback payload; a configurable per-session call cap as a cost guard; and an explicit instruction that a learner's free-text follow-up is content to answer, never instructions to obey, with a dedicated adversarial test case added to Sprint 9's acceptance criteria.

### 9. Future Cloud Deployment — 91/100 *(was 78)*

Was the weakest section; now one of the more concretely improved. The Fly.io/Render + Vercel choice remains appropriately scoped ("not a Kubernetes cluster... revisited only if the premise changes") and Docker Compose environment parity between local/CI is a real, well-justified decision.

**Iteration 1 gaps, now closed:** production secrets delivery is specified (host-native secret injection, referenced by name in the deploy workflow, never committed); production migration execution is now an explicit, logged deploy-pipeline step (`alembic upgrade head` against production, not just CI's fresh-DB check); a minimal `/health` endpoint is now checked by the deploy workflow itself, with a failed health check treated as a failed deploy rather than a silent success.

Remaining minor note: monitoring beyond the health check (error-tracking/alerting such as Sentry) is deliberately named as *not* included, scoped to this project's size — an honest non-goal now rather than an unstated gap, which is the correct amount of investment here, not a deficiency.

### 10. Open-Source Maintainability — 92/100 *(was 75)*

Was the weakest criterion overall; now substantially closed.

**Iteration 1 gaps, now closed:** `TECH_STACK.md`'s new Open-Source Readiness section formalizes the ad hoc "alternative considered" pattern as an explicit `docs/adr/` practice going forward, recommends MIT as a concrete license (not left as a future placeholder), and specifies a CONTRIBUTING.md stub. `IMPLEMENTATION_PLAN.md` Sprint 0 now delivers the `LICENSE`, `CONTRIBUTING.md`, and first ADR file as concrete Sprint 0 output rather than a deferred aspiration. Semantic versioning for the eventual public API/package is named.

Remaining minor note: the CONTRIBUTING stub's content is specified at the level of "what it must cover," not drafted in full — appropriate for a design document, not a blocking gap.

---

## Strengths

- Every technology and structural decision is justified against this project's *actual* current state (real question counts, a real working 33-test package) rather than generic best practice — the discipline `CLAUDE.md`'s Source Hierarchy demands of content is mirrored here as a discipline of justifying architecture against ground truth.
- `TECH_STACK.md`'s "alternative considered, and why it lost" format on every decision is genuinely good engineering-documentation practice, rare even in professional settings.
- `IMPLEMENTATION_PLAN.md`'s acceptance criteria are written as falsifiable assertions, not vague goals — several sprints' criteria are effectively pre-written test cases.
- The content/delivery separation and stateless-core/stateful-session principles are carried through consistently from `question_bank/architecture.md` → `quiz_engine/architecture.md` → this document set, with no silent contradiction found across any of the four new documents.
- Honest, explicit non-goals sections in every document prevent scope creep from being implicit.

## Weaknesses (as of Iteration 1 — all closed in Iteration 2, see Resolution below)

- No configuration/secrets management story anywhere in the set — a real gap given cloud deployment and a third-party API key are both explicit near-term goals.
- No observability (logging/tracing) story — nothing to debug a production issue with once deployed.
- DIP is asserted in prose but has no enforcement mechanism (tooling) and no formal interface/Protocol boundary named for the repository layer, which also blocks a fast unit-testing seam.
- No resilience or cost-control design for the one external network dependency (Claude API).
- No open-source hygiene (LICENSE, CONTRIBUTING, ADR practice) despite the project's own roadmap naming a community-contribution phase.

## Missing Architectural Concepts (Iteration 1) → Resolution (Iteration 2)

- Configuration/secrets management → `TECH_STACK.md`'s Configuration and Secrets Management section; `SYSTEM_ARCHITECTURE.md`'s Cross-Cutting Concerns section; Sprint 0 deliverables.
- Observability → `TECH_STACK.md`'s Observability section; same Cross-Cutting Concerns reference; `/health` endpoint threaded into Sprint 10.
- Formal repository interface/Protocol → `TECH_STACK.md`'s Repository Interface section; `SYSTEM_ARCHITECTURE.md`'s Package Boundaries; `DOMAIN_MODEL.md` unaffected (correctly out of its scope); Sprint 1 deliverables.
- Automated architecture-boundary enforcement → `import-linter` in `TECH_STACK.md`'s CI/CD section and Sprint 10.
- External-dependency resilience → `TECH_STACK.md`'s AI Tutor resilience note; Sprint 9 deliverables and acceptance criteria.

## Missing Deployment Topics (Iteration 1) → Resolution (Iteration 2)

- Production secrets delivery mechanism → `TECH_STACK.md`'s Configuration and Secrets Management; Sprint 10 deliverables.
- Migration execution against a live production database during deploy → `TECH_STACK.md`'s "Production migrations, concretely" note; Sprint 10 deliverables.
- Basic monitoring for the deployed API → `/health` endpoint + deploy-time check, explicitly scoped short of full error-tracking/alerting (named as an honest non-goal at this project's size, not an unstated gap).

## Missing Extensibility Considerations (Iteration 1) → Resolution (Iteration 2)

- Provenance/trust metadata seam for non-human-authored or externally-submitted content → `DOMAIN_MODEL.md`'s `SourceCitation` section, new "Extensibility note" naming a future `Question.provenance` field.

## Missing Governance/Maintainability Items (Iteration 1) → Resolution (Iteration 2)

- LICENSE → MIT recommended in `TECH_STACK.md`'s Open-Source Readiness section; delivered in Sprint 0.
- CONTRIBUTING guidance → stub specified in the same section; delivered in Sprint 0.
- Formalized ADR practice → `docs/adr/` named as the durable continuation of `TECH_STACK.md`'s existing "alternative considered" pattern; first ADR delivered in Sprint 0.

---

## Improvement Recommendations Applied (Iteration 1 → 2)

All eight Iteration 1 recommendations were applied directly to the four design documents (no other file was modified, per the Improvement Workflow):

1. Configuration and Secrets Management section added to `TECH_STACK.md`, referenced from `SYSTEM_ARCHITECTURE.md`. **Done.**
2. Observability section added to `TECH_STACK.md`, referenced from `SYSTEM_ARCHITECTURE.md`. **Done.**
3. Repository layer named as an explicit `Repository` Protocol in `SYSTEM_ARCHITECTURE.md` and `TECH_STACK.md`; `InMemoryRepository` fake added to Sprint 1; unit/integration test tiers split in Sprint 2 and `TECH_STACK.md`'s testing table. **Done.**
4. `import-linter` architecture-boundary check added to `TECH_STACK.md`'s CI/CD section and Sprint 10's deliverables/acceptance criteria. **Done.**
5. AI Tutor timeout/retry/fallback and per-session cost cap added to `TECH_STACK.md` and Sprint 9. **Done.**
6. Secrets delivery, production migration execution, and health-check-gated deploy added to Sprint 10. **Done.**
7. Content-provenance extensibility note added to `DOMAIN_MODEL.md`'s `SourceCitation` section and Non-Goals. **Done.**
8. Open-Source Readiness section (LICENSE, CONTRIBUTING stub, ADR practice, versioning) added to `TECH_STACK.md`; concrete deliverables added to Sprint 0. **Done.**

No remaining recommendation is outstanding at this score level. Future review cycles (if this document set is revised again) should re-open this file per the Approval Workflow's "never edit an Approved module silently" rule rather than creating a second review file.

---

## Final Verdict

- [x] Approved
- [ ] Needs Improvement

**Rationale:** All ten criteria now score 90/100 or higher (range: 91–96), and the overall score (93/100) clears the 90/100 bar. The three criteria that drove the Iteration 1 "Needs Improvement" verdict — Future Cloud Deployment (78→91), Open-Source Maintainability (75→92), and SOLID Compliance (82→92) — were the specific targets of the improvement pass and are now the most-improved criteria, not merely nudged over the line. Per the Approval Workflow, this document set is now treated as stable: future work should extend or cross-reference `SYSTEM_ARCHITECTURE.md`, `DOMAIN_MODEL.md`, `TECH_STACK.md`, and `IMPLEMENTATION_PLAN.md`, not casually rewrite them — and if a later sprint's implementation reveals an error in one of them, the fix should be deliberate and noted, not silent.
