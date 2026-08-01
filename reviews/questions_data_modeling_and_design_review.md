# Question Set Review: Data Modeling and Design (MODEL)

**Reviewed set:** `question_bank/questions/data_modeling_and_design/MODEL-001.yaml` – `MODEL-020.yaml` (20 questions)
**Review date:** 2026-08-01
**Reviewer:** Claude (CDMP Mentor, acting as Technical + DAMA Reviewer per `question_bank/review_process.md`)
**Scope of this review:** Initial quality audit per `question_bank/question_lifecycle.md`. Informs readiness for Gate 1/Gate 2; does not change `review_status`; no improvements applied.

## Set Composition

| Difficulty | Count | Question Types Used |
|---|---|---|
| Beginner | 5 | Multiple Choice (5) |
| Intermediate | 10 | Multiple Choice (4), Scenario-Based (4), Multiple Select (2) |
| Advanced | 5 | Scenario-Based (3), Multiple Select (2) |
| **Total** | **20** | MC: 9, Scenario-Based: 7, Multiple Select: 4 |

Matches the requested 5/10/5 distribution and all three requested question types.

> **Correction (reconciliation pass):** This table originally misreported the question-type sub-counts by one (MC/Scenario-Based). Corrected against a direct field-level recount of `question_bank/questions/data_modeling_and_design/*.yaml`; see `research/question_bank_audit.md`. No question files were affected — this was a review-document error only.

## 1. Accuracy

All 20 correct answers were checked against `knowledge_base/data_modeling_and_design.md`. No factual errors found. Two questions (MODEL-004, MODEL-009) test dimensional-modeling vocabulary (fact table, star/snowflake) correctly tagged `industry_practice_concept` rather than `dama_concept`, consistent with the source module's own explicit note that this vocabulary originates from Kimball's methodology and is referenced, not invented, by DMBOK2. MODEL-019 (Data Vault) is similarly and correctly tagged, with `source_confidence: Medium` reflecting that it rests on an industry-practice enumeration rather than core DMBOK2 text.

## 2. Difficulty

The progression is sound: Beginner questions (MODEL-001–005) test single-term recall directly from a definition. Intermediate questions (MODEL-006–015) consistently require classification against a rule (Logical vs. Physical, which normal form) or a scoped application (choosing a surrogate key, resolving a many-to-many relationship) — appropriately above pure recall. Advanced questions (MODEL-016–020) require multi-decision analysis across a scenario (MODEL-016, MODEL-018) or evaluative judgment about a tradeoff with no single "obviously correct" surface answer (MODEL-017). One note: MODEL-007 (3NF recall) sits at the simpler end of Intermediate and could be defended as Beginner instead — flagged for consideration, not a defect.

## 3. DAMA Alignment

Tagging discipline is consistent and, notably, more nuanced than the Data Governance set: this Knowledge Area contains a higher proportion of `[Industry Practice]`-tagged content (dimensional modeling terms, Data Vault) because the source module itself is explicit that this vocabulary is Kimball/Linstedt-originated rather than DAMA-invented. Every question testing this content correctly reflects that provenance rather than presenting it as DAMA-official — including MODEL-009 and MODEL-019, which are specifically designed to test the *provenance distinction itself* as a Multiple Select item, a good pattern for reinforcing sourcing discipline as exam content, not just as an internal tagging convention.

## 4. Ambiguity

No question was found with two defensible correct answers. MODEL-006 and MODEL-010 both hinge on the same underlying Logical-vs-Physical distinction from different angles (attribute/key presence vs. stakeholder-appropriateness) — intentional reinforcement of the module's own highest-value exam distinction, not accidental overlap. One item worth a second look: MODEL-011's stem describes two documents and asks for a scope match — the phrasing is clear, but a future DAMA reviewer should confirm option ordering doesn't inadvertently favor the correct answer through position bias (both correct components appear in option C specifically).

## 5. Explanation Quality

All 20 explanations state the correct reasoning and provide a specific reason for each incorrect option, consistent with `question_quality_standards.md`, Standards 6–7. Distractors are drawn from real, named confusions the source module documents as Exam Traps (Logical vs. Physical, denormalization-as-mistake, Data Modeling vs. Data Architecture, surrogate vs. natural key) rather than arbitrary wrong answers — this set has an unusually high proportion of distractors traceable directly to a named `Exam Traps` bullet in the source module, which is a strong pattern worth replicating in later Knowledge Areas.

## Summary

The Data Modeling and Design set is accurate, well-distributed, and does an above-average job of testing the DAMA/Industry-Practice provenance distinction as exam content in its own right (MODEL-009, MODEL-019), not just as an internal authoring convention. The two items flagged above (MODEL-007's difficulty placement; MODEL-011's option-ordering check) are minor and suitable for a future improvement pass. No question files were modified as part of this review.
