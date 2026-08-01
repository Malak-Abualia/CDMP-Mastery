# Question Set Review: Metadata Management (META)

**Reviewed set:** `question_bank/questions/metadata_management/META-001.yaml` – `META-020.yaml` (20 questions)
**Review date:** 2026-08-01
**Reviewer:** Claude (CDMP Mentor, acting as Technical + DAMA Reviewer per `question_bank/review_process.md`)
**Scope of this review:** Initial quality audit per `question_bank/question_lifecycle.md`. Informs readiness for Gate 1/Gate 2; does not change `review_status`; no improvements applied.

## Set Composition

| Difficulty | Count | Question Types Used |
|---|---|---|
| Beginner | 5 | Multiple Choice (5) |
| Intermediate | 10 | Multiple Choice (4), Scenario-Based (4), Multiple Select (2) |
| Advanced | 5 | Multiple Choice (1), Scenario-Based (3), Multiple Select (1) |
| **Total** | **20** | MC: 10, Scenario-Based: 7, Multiple Select: 3 |

Matches the requested 5/10/5 distribution and all three requested question types.

> **Correction (reconciliation pass):** This table originally misreported the question-type sub-counts (MC and Scenario-Based were transposed). Corrected against a direct field-level recount of `question_bank/questions/metadata_management/*.yaml`; see `research/question_bank_audit.md`. No question files were affected — this was a review-document error only.

## 1. Accuracy

All 20 correct answers were checked against `knowledge_base/metadata_management.md`. No factual errors identified. The three-category classification (Business/Technical/Operational) — the source module's own highest-value skill — is tested from multiple angles (direct recall in META-001–003; applied classification in META-006–008, META-015), and the "classify by meaning, not storage location" trap is tested twice (META-008, META-015) without redundant phrasing, reinforcing the same principle with two different concrete examples rather than repeating one.

## 2. Difficulty

Progression is sound: Beginner (META-001–005) tests direct category/artifact recall. Intermediate (META-006–015) consistently requires classification of a described, sometimes deliberately tricky example (an ownership field stored in a technical table; a column comment) — correctly above pure recall. Advanced (META-016–020) each require evaluating a real operational or architectural consequence (undocumented downstream breakage, enterprise strategy scoping, a regulatory audit requirement, a storage-layer architectural shift, an instrumentation misconception) rather than a single classification call.

## 3. DAMA Alignment

Tagging is accurate and appropriately mixed: META-012 (data swamp), META-019 (lakehouse-embedded metadata) are correctly tagged `industry_practice_concept` per the source module's own explicit framing of these as industry vocabulary, not DMBOK2-defined terms. META-018's HIPAA content is correctly tagged as a named regulation (`industry_practice_concept`) while the underlying metadata category (Operational) remains `dama_concept`. No question conflates industry tooling/terminology with DAMA-official definitions.

## 4. Ambiguity

No question was found with two defensible correct answers. META-008 and META-015 both test the "classify by meaning, not storage location" principle — reviewed for redundancy and found to use sufficiently distinct scenarios (an ownership field vs. a column comment) that they reinforce rather than duplicate. One item for a future DAMA reviewer to double-check: META-011's phrasing ("data flow diagrams are always more detailed than lineage" as a distractor) inverts the source module's actual claim rather than stating an unrelated falsehood — this is a stronger, more discriminating distractor design, but worth confirming it isn't so close to the correct answer's negation that it reads as a wording trick rather than a knowledge test.

## 5. Explanation Quality

All 20 explanations state the reasoning for the correct classification/answer and a specific reason for every distractor, satisfying `question_quality_standards.md`, Standards 6–7. A notable strength: this set's explanations frequently name the *specific* exam trap being tested (e.g., META-008 and META-010 both explicitly reference "the exam trap" they represent), which is good for a learner reviewing wrong answers but should be checked during formal DAMA Review to confirm it doesn't over-telegraph the pattern in a way that reduces future test validity if the same trap phrasing recurs verbatim across many questions.

## Summary

The Metadata Management set is accurate, well-distributed, and gives strong, repeated coverage to this Knowledge Area's two highest-value skills: three-category classification and the lineage-vs-data-flow-diagram / lineage-composition distinctions. The two items flagged above (META-011's distractor phrasing; explanation phrasing that names traps explicitly) are minor stylistic considerations for a future improvement pass, not defects. No question files were modified as part of this review.
