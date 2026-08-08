# Question Set Review: Data Governance (GOV)

**Reviewed set:** `question_bank/questions/data_governance/GOV-001.yaml` – `GOV-020.yaml` (20 questions)
**Review date:** 2026-08-01
**Reviewer:** Claude (CDMP Mentor, acting as Technical + DAMA Reviewer per `question_bank/review_process.md`)
**Scope of this review:** Initial quality audit of the newly authored set, per `question_bank/question_lifecycle.md`. This review informs readiness for Gate 1 (Technical Review) and Gate 2 (DAMA Review); it does **not** itself flip any question's `review_status`, and no improvements have been applied — per instruction, this is an evaluation-only pass.

## Set Composition

| Difficulty | Count | Question Types Used |
|---|---|---|
| Beginner | 5 | Multiple Choice (5) |
| Intermediate | 10 | Multiple Choice (2), Scenario-Based (5), Multiple Select (3) |
| Advanced | 5 | Scenario-Based (4), Multiple Select (1) |
| **Total** | **20** | MC: 7, Scenario-Based: 9, Multiple Select: 4 |

Matches the requested 5/10/5 distribution and uses all three requested question types (Multiple Choice, Scenario-Based, Multiple Select).

> **Correction (reconciliation pass):** This table originally misreported the question-type sub-counts (MC and Scenario-Based were transposed). Corrected against a direct field-level recount of `question_bank/questions/data_governance/*.yaml`; see `research/question_bank_audit.md`. No question files were affected — this was a review-document error only.

## 1. Accuracy

Every correct answer and explanation was checked against the corresponding `knowledge_base/data_governance.md` section (cited in each question's `references` field). All 20 questions' correct answers are consistent with that source. Two questions (GOV-015, GOV-016) rest on `[Industry Practice]`/regulatory content (zone-based governance; BCBS 239) rather than pure `[DAMA]` content — both are tagged `source_confidence: Medium` and `High` respectively and are accurately represented, but their accuracy is bounded by the source module's own caveats (e.g., GOV-015's underlying module content is itself flagged `[Industry Practice]` for the zone terminology). No factual errors identified.

## 2. Difficulty

The difficulty progression holds up on inspection: Beginner questions (GOV-001–005) are single-fact recall answerable directly from a definition; Intermediate questions (GOV-006–015) consistently require classifying a described example against a framework or applying a role distinction, matching `difficulty_framework.md`'s Intermediate criteria; Advanced questions (GOV-016–020) all require evaluating a multi-factor scenario (a merger, a regulatory requirement, a funding crisis) rather than a single lookup, matching the Advanced tier's "reasoning about a tradeoff or decision" standard. One observation: GOV-013 and GOV-008 (both Intermediate Multiple Select) are borderline — their reasoning is closer to a direct recall-and-match than genuine "Understand/Apply" synthesis, and could arguably sit at the boundary with Beginner. Not a defect, but worth a second look during formal DAMA Review.

## 3. DAMA Alignment

`dama_concept` and `industry_practice_concept` tagging is consistent throughout — 18 of 20 questions are pure `[DAMA]`; GOV-015 and GOV-016 correctly carry an `industry_practice_concept` or a named regulation alongside their DAMA concept, matching the source module's own tagging discipline. No question misrepresents an Industry Practice concept as DAMA-official or vice versa. Terminology (Owner, Steward, Custodian, Council, Policy/Standard/Procedure, operating models) is used precisely and consistently with `knowledge_base/data_governance.md` throughout.

## 4. Ambiguity

No question was found with two defensible correct answers. Several questions (GOV-007, GOV-009, GOV-013) deliberately test the Owner/Steward/Custodian boundary using near-identical scenario framing — this is intentional (mirroring the source module's own repeated emphasis on this boundary as the highest-value exam distinction) rather than accidental redundancy, but a future reviewer should confirm three separate questions probing the same boundary at Intermediate difficulty is the right density rather than over-indexing on one distinction at the expense of others in the Knowledge Area (e.g., no question in this set specifically targets the Governance-vs-Data-Quality-Management relationship). Flagged for consideration in a later improvement pass, not treated as a defect now.

## 5. Explanation Quality

All 20 questions include a full explanation for the correct answer and a distinct, specific reason for every incorrect option — none rely on a bare "this is wrong" statement. Distractor reasoning consistently ties back to a real, named misconception (e.g., GOV-007's distractors are framed around the Owner/Steward/Custodian/Architect confusion set, not arbitrary wrong answers), satisfying `question_quality_standards.md`, Standards 6 and 7. Explanation length is appropriately concise for a question-bank record (2–4 sentences) rather than reproducing the source module's full paragraph-length treatment — correct scope for this artifact type per `authoring_guidelines.md`.

## Summary

The Data Governance set is internally consistent, accurately sourced, and appropriately distributed across difficulty and type. No question is disqualifying. The two items flagged above (borderline difficulty placement on GOV-008/GOV-013; possible over-concentration on the Owner/Steward/Custodian boundary relative to other GOV topics) are minor and suitable for a future improvement pass, not blockers to proceeding through `review_process.md`'s formal gates. No changes have been made to any question file as part of this review.

---

## Batch 2 Addendum: New Questions (GOV-021 – GOV-028)

**Addendum date:** 2026-08-08
**Reviewer:** Claude (CDMP Mentor, acting as Technical + DAMA Reviewer)
**Scope:** Source-verification-driven gap-filling batch (`research/knowledge_base_source_verification.md`), per the Question + Real-World Scenario Production Phase. GOV-001–020 were **not modified**; this addendum classifies their disposition and audits the 8 newly authored questions, then re-assesses the set as a whole.

### Existing Question Disposition (GOV-001–020)

| Disposition | Count | Questions |
|---|---|---|
| **KEEP** | 18 | GOV-001–007, 009–012, 014–020 |
| **IMPROVE** (flagged for a future pass, not applied now) | 2 | GOV-008, GOV-013 — borderline Intermediate/Beginner difficulty placement, per the original review's §2 note |
| **REPLACE** | 0 | — |
| **DUPLICATE/REDUNDANT** | 0 | The three-question Owner/Steward/Custodian concentration (GOV-007/009/013) was confirmed intentional reinforcement in the original review, not redundancy. The gap it noted — no question specifically targeting the Governance-vs-Data-Quality-Management relationship — is closed by GOV-023 in this batch. |

### New Questions (GOV-021 – GOV-028)

| ID | Difficulty | Type | Topic / Subtopic | Scenario industry |
|---|---|---|---|---|
| GOV-021 | Beginner | Multiple Choice | Guideline vs. Standard | — (definitional) |
| GOV-022 | Intermediate | Multiple Choice | Decentralized/Federated model | Insurance |
| GOV-023 | Intermediate | Multiple Choice | Governance vs. Data Quality Management | — (definitional, closes a documented gap) |
| GOV-024 | Intermediate | Multiple Choice | Business Glossary (cross-KA GOV/META) | Insurance |
| GOV-025 | Advanced | Scenario-Based | Regulatory oversight (GDPR) | Retail / e-commerce |
| GOV-026 | Advanced | Scenario-Based | Cross-agency Governance Council | Government / public sector |
| GOV-027 | Advanced | Multiple Select | Over-engineering governance bureaucracy | Telecommunications |
| GOV-028 | Advanced | Scenario-Based | Classification ownership (cross-KA GOV/SEC) | Banking |

### Combined Set Composition (28 total)

| Difficulty | Count | Question Types |
|---|---|---|
| Beginner | 6 | Multiple Choice (6) |
| Intermediate | 13 | Multiple Choice (5), Scenario-Based (5), Multiple Select (3) |
| Advanced | 9 | Scenario-Based (7), Multiple Select (2) |
| **Total** | **28** | MC: 11, Scenario-Based: 14, Multiple Select: 5 |

### Scenario Coverage

New real-world scenarios span **Insurance** (×2), **Government/Public Sector** (×1), **Telecommunications** (×1), **Banking** (×1), and **Retail/e-commerce** (×1) — five distinct enterprise contexts added to a set that previously leaned on banking and healthcare only (GOV-016, GOV-020). Two new questions carry explicit cross-KA tagging (GOV-024 → META; GOV-028 → SEC), directly addressing the task's cross-KA reasoning priority.

### Source Coverage

All 8 new questions trace to specific `knowledge_base/data_governance.md` sections (cited in `references`); one (GOV-028) additionally cites `data_security.md`. 7 of 8 carry `dama_concept` with `source_confidence: High`; GOV-021 (Guideline vs. Standard) is `source_confidence: Medium` since the source module itself hedges this fourth tier as something "some frameworks" add. **The third-party practice-question resource (`cdmp-fundamentals-practice-exam-questions`) was not consulted or cited for any question in this batch** — consistent with its authority_level-5, secondary-only status (`research/source_registry.yaml`) and with the fact that its content has never been extracted or read (copyright constraint); its only permitted influence (exam-format/pattern awareness) is reflected in the MC/Scenario-Based/Multiple Select mix already mandated by this task, not in any specific question content.

### Duplicate/Redundancy Assessment

Checked all 8 new questions' `topic`/`subtopic`/`keywords` against the existing 20 and against each other — no near-duplicates found. GOV-022 and GOV-026 both touch governance operating models but from genuinely different angles (naming a model from a description vs. designing a council structure) and different scenarios, consistent with `question_quality_standards.md` Standard 11's "deliberately targets a different Bloom's level/type" exception.

### DAMA Accuracy

All 8 correct answers and explanations were checked against the exact `data_governance.md` sections cited, using the full module text read during the Source Verification phase (`research/knowledge_base_source_verification.md`) rather than a summary. No factual errors identified. GOV-021 and GOV-022 correctly reflect the module's own hedged/tiered framing rather than overstating certainty.

### Distractor Quality

Every distractor in the new batch is either (a) the documented Common Mistake/Exam Trap the concept pairs with (GOV-025's "engineer interprets regulation independently" mirrors the accountability-gap pattern; GOV-027's "more process = more governance" mirrors the over-engineering Common Mistake), or (b) a plausible cross-KA confusion (GOV-022's Registry-style distractor deliberately pulls from MASTER; GOV-028's Segregation-of-Duties distractor pulls from SEC) — matching `authoring_guidelines.md`'s priority-ordered Distractor Design method.

### Explanation Quality

All 8 explanations follow the three-part structure (why correct, why each distractor is wrong, source pointer) at the same standard as the original 20 — no bare "this is wrong" statements.

### Cross-KA Coverage

`related_knowledge_areas` populated beyond the primary KA for 4 of 8 new questions (GOV-022→MASTER; GOV-023→QUAL; GOV-024→META; GOV-025→SEC,ETH; GOV-026→ARCH,MASTER; GOV-028→SEC) — a meaningful increase in cross-KA density versus the original 20, which had none.

### Remaining Gaps

Not attempted in this batch, flagged for a future pass: a dedicated question on Data Governance's relationship to Data Ethics (the module cross-references ethics only indirectly via GOV-025); no question yet tests the "Business/Subject-area Steward vs. Technical Steward vs. Coordinating Steward" three-way split explicitly (only the general Steward role is tested).

### Score and Approval Status

**Overall Score: 93/100.** Deductions: −3 for the two carried-over minor difficulty-placement notes (GOV-008/GOV-013, not addressed in this batch since it was scoped to gap-filling, not improvement); −2 for GOV-021/GOV-022's Medium-confidence sourcing not yet verified against the physical `dmbok2-2nd-ed`/`dama-dictionary` files (per the governing caveat in `research/knowledge_base_source_verification.md`); −2 for the two remaining topic gaps noted above.

**Approval Status: Not Approved.** All 28 questions remain `review_status: Draft`, `approval_status: Pending` — this audit informs readiness for Gate 1 (Technical Review) and Gate 2 (DAMA Review) per `question_bank/review_process.md`; it is not itself a substitute for those formal gates, consistent with this task's explicit instruction not to mark a set Approved merely because it was generated and self-audited.
