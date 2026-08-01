# Question Set Review: Reference and Master Data (MASTER)

**Reviewed set:** `question_bank/questions/reference_and_master_data/MASTER-001.yaml` – `MASTER-020.yaml` (20 questions)
**Review date:** 2026-08-01
**Reviewer:** Claude (CDMP Mentor, acting as Technical + DAMA Reviewer per `question_bank/review_process.md`)
**Scope of this review:** Initial quality audit per `question_bank/question_lifecycle.md`. Informs readiness for Gate 1/Gate 2; does not change `review_status`; no improvements applied.

## Set Composition

| Difficulty | Count | Question Types Used |
|---|---|---|
| Beginner | 5 | Multiple Choice (5) |
| Intermediate | 10 | Multiple Choice (5), Scenario-Based (3), Multiple Select (2) |
| Advanced | 5 | Scenario-Based (3), Multiple Select (2) |
| **Total** | **20** | MC: 10, Scenario-Based: 6, Multiple Select: 4 |

Matches the requested 5/10/5 distribution and all three requested question types.

## Non-Duplication Check

Per `question_quality_standards.md`, Standard 11, this set was checked against `knowledge_base/reference_and_master_data.md`'s own existing 15 Quiz Questions (Section 13) to confirm no direct duplication. All 20 questions here are original: they use different scenarios, different wording, and in several cases test content the source module's own quiz did not cover (e.g., Value Domain, Master Data Types/Party, Data Sharing Agreements, MDM Success Metrics — all added to the module in its post-review revision but not represented in its original 10-question quiz). No overlap found.

## 1. Accuracy

All 20 correct answers were checked against `knowledge_base/reference_and_master_data.md`. No factual errors identified. This set draws on the module's most recently added content (Master Data Types/Party generalization, Value Domain, Data Sharing Agreements, MDM Success Metrics, and the MDM-vs-Metadata-Management trap) at a higher proportion than the other five sets reviewed so far, which is appropriate given this module was itself revised to close exactly these gaps — the question set directly exercises the fixes from that revision.

## 2. Difficulty

Progression is sound: Beginner (MASTER-001–005) tests direct definitional recall of the core vocabulary (Reference Data, Master Data, Golden Record, Survivorship Rules, Value Domain). Intermediate (MASTER-006–015) consistently requires classification against the Reference-vs-Master test or an MDM-style identification from a described behavior — correctly above pure recall, and MASTER-007 in particular (the Product/Product-Category overlap case) is a well-targeted test of the hardest classification edge case the source module documents. Advanced (MASTER-016–020) each require a multi-factor evaluative judgment (a regulatory implementation-style tradeoff, per-attribute survivorship design reasoning, a clinical risk tradeoff, a per-domain style differentiation, and a governance-completeness check) — correctly calibrated above the single-classification Intermediate tier.

## 3. DAMA Alignment

Tagging is accurate throughout, including correct use of `[DAMA + Industry Practice]`-adjacent framing inherited from the source module for Golden Record and MDM Implementation Styles (reflected here via `source_confidence: Medium` on MASTER-011 and MASTER-013, matching the module's own hedging on Master Data Types and MDM Success Metrics as less firmly DMBOK2-enumerated content). MASTER-006 and MASTER-016 correctly tag named external standards (ISO 4217, BCBS 239) as `industry_practice_concept` rather than DAMA-official.

## 4. Ambiguity

No question was found with two defensible correct answers. MASTER-008 and MASTER-009 both test MDM-style identification from behavioral description (Registry vs. Coexistence) using a parallel structure — intentional reinforcement of the four-style framework, not accidental overlap, and the two styles tested are correctly the most commonly confused pair (a virtual layer vs. a synchronized physical layer). MASTER-015, testing the MDM-vs-Metadata-Management name-confusion trap, was checked for fairness — the distractors are structurally parallel (subset/superset framings) rather than one being obviously absurd, which is good distractor design rather than an ambiguity risk.

## 5. Explanation Quality

All 20 explanations state the reasoning for the correct answer and a specific reason for every distractor, satisfying `question_quality_standards.md`, Standards 6–7. Advanced-tier explanations in particular (MASTER-016, MASTER-018, MASTER-020) do well at explicitly naming the underlying principle being tested (regulatory-driven style selection, false-positive clinical risk, the Owner/Custodian boundary) rather than only restating the scenario, giving each explanation real standalone teaching value.

## Summary

The Reference and Master Data set is accurate, well-distributed, confirmed non-duplicative against the source module's existing quiz content, and gives strong, targeted coverage to the concepts added during that module's most recent revision (Value Domain, Master Data Types, Data Sharing Agreements, MDM Success Metrics, and the MDM/Metadata-Management trap) — directly reinforcing the fixes that took the module from 86 to 93 in its own review cycle. No disqualifying issues were found. No question files were modified as part of this review.

---

## Cross-Set Note

This completes Phase 1 authoring for all six Approved Knowledge Areas (120 questions total: GOV, MODEL, ARCH, QUAL, META, MASTER, 20 each). Per this task's scope, no improvements have been attempted for any set — each of the six per-KA reviews above documents minor, non-blocking observations (difficulty-placement checks, sequencing/repetition notes, distractor-phrasing checks) reserved for a future improvement pass, consistent with `question_bank/review_process.md`'s Gate 1/Gate 2 structure. No question file was modified during authoring-review; every question remains in `review_status: Draft`, `approval_status: Pending`, awaiting formal Gate 1/Gate 2/Approval processing.
