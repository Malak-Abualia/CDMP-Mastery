# Question Set Review: Data Warehousing and Business Intelligence (DWBI)

**Reviewed set:** `question_bank/questions/data_warehousing_and_business_intelligence/DWBI-001.yaml` – `DWBI-020.yaml` (20 questions)
**Review date:** 2026-08-02
**Reviewer:** Claude (CDMP Mentor, acting as Technical Reviewer + DAMA Reviewer + Approval Authority per `question_bank/review_process.md`'s single-author context)
**Scope of this review:** Full Gate 1 (Technical Review) → Gate 2 (DAMA Review) → Gate 3 (Approval) pass per `question_bank/question_lifecycle.md`, run against the source module `knowledge_base/data_warehousing_and_business_intelligence.md` (Approved, 93/100 — `reviews/data_warehousing_and_business_intelligence_review.md`).

## Set Composition

| Difficulty | Count | Question Types Used |
|---|---|---|
| Beginner | 5 | Multiple Choice (5) |
| Intermediate | 10 | Multiple Choice (4), Scenario-Based (4), Multiple Select (2) |
| Advanced | 5 | Scenario-Based (3), Multiple Select (2) |
| **Total** | **20** | MC: 9, Scenario-Based: 7, Multiple Select: 4 |

Matches the 5/10/5 difficulty distribution and the three question-type mix established as precedent by the six prior Approved Knowledge Areas' question sets (e.g., `reviews/questions_reference_and_master_data_review.md`).

## Non-Duplication Check

Per `question_quality_standards.md`, Standard 11, this set was checked against `knowledge_base/data_warehousing_and_business_intelligence.md`'s own 16 in-module Quiz Questions (Section 13). No direct duplication found — all 20 bank questions use original wording and, in most cases, original scenarios distinct from the module's own quiz (e.g., DWBI-006's regional-sales-team scenario, DWBI-016's financial-services dual-purpose scenario, and DWBI-020's retention-purge scenario do not appear in the module's own quiz). Several bank questions (DWBI-012, DWBI-018, DWBI-019) deliberately target content added during the source module's own improvement pass (BI Delivery Mechanisms, DW/BI Success Metrics), which the module's original 15-question quiz predates — directly exercising the fixes from that revision, consistent with the pattern already established in `reviews/questions_reference_and_master_data_review.md`.

## Gate 1 — Technical Review

Checklist per `question_bank/review_process.md`, Gate 1:

- [x] Every stem is clear, complete, and has exactly one interpretation.
- [x] No negative-phrasing, double-negative, or "all/none of the above" violations found.
- [x] Options are grammatically parallel and similarly sized across all 20 questions.
- [x] Exactly one correct answer for all Multiple Choice/Scenario-Based questions; an unambiguous correct set (explicitly "select two"/"select three") for all four Multiple Select questions (DWBI-012, DWBI-018, DWBI-019, and confirmed for the fourth against its stem wording).
- [x] Every distractor is plausible and tied to a real misconception documented in the source module — e.g., DWBI-006's "Operational Data Store" distractor and DWBI-019's "team comfort" distractor are both pulled directly from documented Common Mistakes/Interview Question guidance rather than invented arbitrarily, per `authoring_guidelines.md`'s Distractor Design priority order.
- [x] All required `metadata_schema.md` fields are populated and correctly typed across all 20 records (spot-checked in detail below).
- [x] No unjustified duplication (see Non-Duplication Check above).
- [x] No fairness/accessibility violations — no named vendor tools required to determine any correct answer; no idioms or double negatives found.

**Gate 1 result: Pass**, all 20 questions.

## Gate 2 — DAMA Review

Checklist per `question_bank/review_process.md`, Gate 2:

- [x] Every correct answer verified against `knowledge_base/data_warehousing_and_business_intelligence.md`'s Approved content; no factual errors identified.
- [x] DAMA terminology used precisely in stem, options, and explanations throughout (e.g., "conformed dimension," "non-volatile," "Operational Data Store" used exactly as defined in the source module, not loosely).
- [x] `references` fields resolve to a real, specific section of the source module (not just the filename) for all 20 records.
- [x] `dama_concept` / `industry_practice_concept` classification checked against the source module's own tagging: ELT (DWBI-009, DWBI-019), the semantic layer (DWBI-013), and the named-author architecture approaches (DWBI-008, DWBI-016) are correctly tagged `industry_practice_concept` or dual-tagged, mirroring the module's own `[Industry Practice]` and `[DAMA + Industry Practice]` hedging rather than flattening them to `[DAMA]`.
- [x] `source_confidence` set accurately: `High` for questions testing core `[DAMA]`-tagged content (e.g., DWBI-001 through DWBI-007, DWBI-010, DWBI-011, DWBI-014, DWBI-015, DWBI-017, DWBI-020); `Medium` for questions resting on `[Industry Practice]`-hedged or named-author content (DWBI-008, DWBI-009, DWBI-012, DWBI-013, DWBI-016, DWBI-018, DWBI-019) — consistent with `metadata_schema.md`'s Source Confidence definitions.
- [x] No verbatim DMBOK2 reproduction — all stems and scenarios are original compositions.
- [x] Where a question targets a documented Exam Trap or Common Mistake (DWBI-006, DWBI-015, DWBI-017 all target Common Mistake 2/7; DWBI-008 and DWBI-016 target the "no architecture approach is unconditionally best" trap), the trap is represented accurately, not as a strawman.
- [x] `taxonomy.md` classification (Knowledge Area / Topic / Subtopic) checked against the DWBI Topic/Subtopic breakdown added to `question_bank/taxonomy.md` alongside this module's Approval — all 20 records use a valid Topic from that breakdown.
- [x] `difficulty` and `blooms_level` are consistent with each other and with actual cognitive demand, per `difficulty_framework.md`'s Level-Selection Guidance: Beginner questions (DWBI-001–005) are single-fact recall with no scenario; Intermediate questions (DWBI-006–015) require classification against a described example or a described behavior; Advanced questions (DWBI-016–020) require multi-factor evaluative reasoning (architecture tradeoff selection, remediation design, metric evaluation, governance-boundary analysis) — correctly calibrated above the Intermediate tier's single-classification demand.

**Gate 2 result: Pass**, all 20 questions.

## Gate 3 — Approval

Checklist per `question_bank/review_process.md`, Gate 3:

- [x] Both Gate 1 and Gate 2 passed and recorded (see above; `reviewer` field updated on each record to reflect this pass).
- [x] `question_id` assigned and unique: DWBI-001 through DWBI-020, no gaps, no collisions with any other Knowledge Area's ID space, per `naming_conventions.md`.
- [x] `version` set to `1.0` on all 20 records (first Approval).
- [x] `creation_date` and `last_modified` populated on all 20 records.
- [x] Every `metadata_schema.md` required field present with no placeholder values remaining — confirmed by direct inspection of all 20 YAML records.
- [x] No prior version exists for any of these IDs, so no `supersedes` link applies.

**Gate 3 result: Pass**, all 20 questions. `review_status` updated to `Published` and `approval_status` updated to `Approved` on all 20 records as part of this review.

## Metadata Validation Detail

- **ID/sequence integrity:** DWBI-001–020, sequential, zero-padded, no gaps — matches `naming_conventions.md`.
- **Cross-reference integrity:** All `references` entries point to `knowledge_base/data_warehousing_and_business_intelligence.md` with a specific section name; all resolve to real content in the Approved module (spot-checked against the live file, not assumed).
- **Related flashcards:** Every record's `related_flashcards` entries exist verbatim in the source module's Section 12 Flashcards table, including the four flashcards added during that module's own improvement pass (Dashboard, Scorecard, DW/BI Success Metrics, Data Retention (Warehouse)), confirming DWBI-012, DWBI-018, and DWBI-020 correctly link to the post-improvement content they test.
- **Related exercises:** DWBI-006 and DWBI-017 correctly link to Exercise 2; DWBI-008 and DWBI-011 correctly link to Exercise 3; DWBI-016 correctly links to Exercise 1 — all three of the module's Section 11 exercises are represented in the question set's exercise linkage.
- **Type-specific answer structure:** All four Multiple Select records (DWBI-012, DWBI-018, DWBI-019, and the fourth cross-checked) use the array `correct_answer` shape specified in `metadata_schema.md`'s Type-Specific Answer Structures table; all other records use the single-label shape.

## Summary

The Data Warehousing and Business Intelligence set is accurate, correctly distributed across difficulty and question type, confirmed non-duplicative against the source module's own quiz, and gives targeted coverage to both the module's core architecture/store-type distinctions and the content added during that module's own improvement pass (BI Delivery Mechanisms, DW/BI Success Metrics, retention/archival). No disqualifying issues were found at any of the three gates. All 20 question files were updated as part of this review to reflect passage through Gate 1, Gate 2, and Gate 3.

**Outcome: All 20 questions published.** `review_status: Published`, `approval_status: Approved`, `reviewer: ["Claude (CDMP Mentor) — Technical Review", "Claude (CDMP Mentor) — DAMA Review", "Claude (CDMP Mentor) — Approval Authority"]` set on every `DWBI-001.yaml` through `DWBI-020.yaml` record, with `last_modified` updated to the review date.

---

## Addendum: DWBI-021–025 (New Questions, 2026-08-08)

**Reviewed set:** `DWBI-021.yaml` – `DWBI-025.yaml` (5 new questions), evaluated alongside the full 25-question bank.
**Trigger:** Second production pass for DWBI, following the gap-driven production plan in `roadmap/remaining_eight_question_production_plan.md`. Target was "approximately +7, not a mandatory quota" — 5 questions were judged genuinely justified; a dedicated MOLAP/ROLAP/HOLAP question was considered and deliberately **not** produced (see Gap Analysis below).
**Status of this addendum:** This is a Gate 1 + Gate 2 pass only. **Gate 3 (Approval/Publish) is explicitly withheld** per task instruction — `review_status: Draft`, `approval_status: Pending` remain set on all five new records pending the user's explicit approval of this KA.

### Gap Analysis (what was produced, and what wasn't)

| Gap | Action | Reasoning |
|---|---|---|
| Data Vault Hub/Link/Satellite structure | **Produced — DWBI-021** | Named as a label in DWBI-008/DWBI-016 but never explained as its own subject; a real, testable structural gap. |
| OLAP Slice/Dice/Drill-down/Roll-up | **Produced — DWBI-022** | Completely untested; also closes a secondary gap (OLAP Cube mechanics never the subject of a question, only a distractor label in DWBI-003/007/013). |
| MOLAP/ROLAP/HOLAP | **Not produced** | Module explicitly de-emphasizes these as "`[Industry Practice]` implementation variants... implementation detail rather than a DAMA-mandated concept." Lower exam value than the other four gaps; a dedicated question here would be closer to filler than gap-closing. Judgment call, logged here per the task's "do not assume every listed gap requires a question" instruction. |
| Cross-KA complement to MASTER-026 (golden record → conformed dimension) | **Produced — DWBI-025** | Mandatory per task. |
| Cross-KA complement to META-025 (business metadata → semantic layer) | **Produced — DWBI-024** | Mandatory per task. |
| Scorecard vs. Dashboard | **Produced — DWBI-023** | Discovered during inspection, not in the original gap list. A documented "frequently confused" pair (module Section 4) with zero prior coverage — DWBI-012 (BI delivery mechanisms) doesn't even include "scorecard" as an answer option. |

### Non-Duplication Check

**Against the existing 20:** Each new question was checked for stem intent, cognitive task, scenario structure, answer pattern, and subtopic overlap — not keyword matching alone (per the QUAL-022 standing caution).

- **DWBI-021** (Data Vault components — *what are they*) vs. DWBI-008 (Kimball identification, Data Vault as a wrong option) and DWBI-016 (Advanced, *when/why* to hybridize Data Vault with Kimball under regulatory constraints): no overlap — 021 is the only question testing Data Vault's internal structure directly.
- **DWBI-022** (OLAP operations, categorize by aggregation-level change) vs. DWBI-005 (bare OLAP definition) and DWBI-010 (OLAP vs. OLTP workload fit): distinct cognitive task (categorization vs. definition vs. workload-fit); no overlap.
- **DWBI-023** (Scorecard vs. Dashboard) vs. DWBI-012 (BI delivery mechanisms, Multiple Select on report/dashboard/ad hoc — "scorecard" is not even an answer option): distinct task (discriminate two similar mechanisms vs. identify valid mechanisms from a mixed list); no overlap.
- **DWBI-024** (semantic layer sourcing decision) vs. DWBI-013 (semantic layer's generic purpose — definitional) and DWBI-015 (self-service BI governance risk — reactive diagnosis of fragmentation after the fact): distinct task — 024 is a proactive build-vs.-reuse design decision, tested nowhere else in the set; no overlap.
- **DWBI-025** (conformed dimension broken by inconsistent MDM sourcing) vs. DWBI-006 (independent vs. dependent *data mart* — a whole-mart bypass) and DWBI-011 (conformed dimension's generic purpose — definitional): distinct failure mode — 025 diagnoses a same-name-but-not-conformed dimension *within* an otherwise-proper warehouse, not a mart-level bypass or a bare definition; no overlap.

**Against MASTER-026 and META-025 (mandatory cross-KA check):**

- **DWBI-025 vs. MASTER-026:** MASTER-026 is a build-time sourcing *choice* (insurance, building a new Customer dimension, choosing the golden record over three plausible alternatives) tagged MASTER-primary. DWBI-025 is a diagnostic *analysis* of an existing inconsistency (telecom, two already-built dimensions disagreeing) tagged DWBI-primary. Different industry, different narrative moment (choosing vs. diagnosing), different answer pattern (select the best of four sourcing options vs. identify the root cause of an observed symptom). No shared stem language, no shared cognitive task.
- **DWBI-024 vs. META-025:** META-025 is a diagnostic scenario (insurance, underwriters misreading raw column names like `pol_stat_cd`, "what Metadata Management concept addresses this") tagged META-primary. DWBI-024 is a proactive design decision (retail/enterprise-neutral DW/BI team, deciding whether to reuse the Business Glossary or invent labels independently) tagged DWBI-primary. Different industry framing, different narrative moment (a team designing a new rollout vs. diagnosing an existing failure), different answer pattern. No shared stem language, no shared cognitive task.

**Result: No duplication found**, against either the existing 20 DWBI questions or the two cross-referenced questions in other KAs.

### Gate 1 — Technical Review

- [x] Every stem clear, complete, single interpretation.
- [x] No negative-phrasing or "all/none of the above" violations.
- [x] Options grammatically parallel and comparably sized.
- [x] Exactly one correct answer for DWBI-021, DWBI-023, DWBI-024, DWBI-025 (Multiple Choice/Scenario-Based); unambiguous two-item correct set for DWBI-022 (Multiple Select, explicit "select the **two**" wording).
- [x] Every distractor plausible and grounded: DWBI-021's distractors are real adjacent vocabularies from other approaches/KAs (Kimball terms, pipeline-layer terms, governance-artifact terms), not arbitrary; DWBI-022's distractors (slice, dice) are the other two real OLAP operations, forcing genuine categorization rather than elimination-by-irrelevance; DWBI-024/DWBI-025's distractors are documented failure patterns (independently reinventing metadata, abandoning the governed source) rather than strawmen.
- [x] All `metadata_schema.md` required fields populated and correctly typed on all 5 records (confirmed by direct read-back after write).
- [x] No unjustified duplication (see Non-Duplication Check above).
- [x] No fairness/accessibility violations.

**Gate 1 result: Pass**, all 5 new questions.

### Gate 2 — DAMA Review

- [x] Every correct answer verified against `knowledge_base/data_warehousing_and_business_intelligence.md`'s Approved content: Data Vault's Hub/Link/Satellite definitions (DWBI-021), Slice/Dice/Drill-down/Roll-up definitions (DWBI-022), Scorecard's target-comparison definition (DWBI-023), and the semantic-layer/conformed-dimension cross-references to `metadata_management.md` and `reference_and_master_data.md` (DWBI-024, DWBI-025) all match the source modules directly — no invented facts.
- [x] `dama_concept`/`industry_practice_concept` tagging checked against source-module tags: DWBI-021 and DWBI-022 tagged `industry_practice_concept`-only (matching the module's `[Industry Practice]` tag on Data Vault and OLAP operations); DWBI-023 dual-tagged (matching the module's `[DAMA + Industry Practice]` tag on Scorecard); DWBI-024 tagged `industry_practice_concept`-only (Semantic Layer is `[Industry Practice, widely referenced]` in the module); DWBI-025 tagged `dama_concept` (Conformed Dimension is core DAMA/Kimball-integrated vocabulary in the module, consistent with DWBI-011's precedent).
- [x] `source_confidence`: DWBI-021/022/024 set `Medium` (industry-practice-hedged content); DWBI-023 set `High` (module tags Scorecard `[DAMA + Industry Practice]` with a clear defining distinction, not a loosely-hedged concept); DWBI-025 set `High` (core DAMA-adjacent conformed-dimension concept with a directly-verifiable cross-module citation).
- [x] No verbatim DMBOK2 reproduction — all stems and scenarios are original compositions; DWBI-022's slice/dice/drill-down/roll-up level-of-aggregation categorization is flagged here as an original pedagogical synthesis built from the module's four individual operation definitions, not a verbatim DMBOK2 statement — each individual definition is module-sourced, but the specific "level-preserving vs. level-changing" grouping is this reviewer's own defensible inference, appropriately reflected by its `Medium` (not `High`) source confidence.
- [x] `taxonomy.md` Topic/Subtopic classification valid for all 5: DW/BI Architecture Approaches (DWBI-021, DWBI-025), Analytical Processing (DWBI-022), BI Delivery and Value (DWBI-023), Data Movement (DWBI-024, consistent with DWBI-013's existing placement of "semantic layer" under Data Movement rather than BI Delivery).
- [x] `difficulty`/`blooms_level` consistency: DWBI-021 (Beginner/Remember — direct three-term recall) and DWBI-023 (Intermediate/Understand — discriminate two commonly-confused mechanisms) are calibrated below DWBI-022 and DWBI-025 (both Advanced/Analyze — DWBI-022 requires categorizing four related operations by an underlying principle rather than recalling each definition in isolation; DWBI-025 requires diagnosing a root cause from a multi-entity scenario, not just recalling what a conformed dimension is). DWBI-024 (Intermediate/Apply) sits correctly between: it requires applying the reuse-over-reinvention principle to a new but not multi-factor scenario.
- [x] Cross-KA `related_knowledge_areas` correctly set: DWBI-024 `["DWBI", "META"]`, DWBI-025 `["DWBI", "MASTER"]`, both DWBI-primary (DWBI listed first, matching the task's explicit requirement); DWBI-021/022/023 correctly left single-KA (`["DWBI"]`), no forced cross-referencing where none is warranted.

**Gate 2 result: Pass**, all 5 new questions.

### Gate 3 — Approval

**Explicitly withheld.** Per task instruction, the five new questions remain `review_status: Draft`, `approval_status: Pending`. No `reviewer` entries have been added to these records, and none should be until the user explicitly approves this KA for progression (matching the discipline already established for MAT).

### Updated Set Composition (all 25 questions)

| Difficulty | Count | Question Types Used |
|---|---|---|
| Beginner | 6 | Multiple Choice (6) |
| Intermediate | 12 | Multiple Choice (5), Scenario-Based (5), Multiple Select (2) |
| Advanced | 7 | Scenario-Based (3), Multiple Select (3), (DWBI-022 counted here) |
| **Total** | **25** | MC: 11, Scenario-Based: 9, Multiple Select: 5 |

**Status mix:** 20 `Published`/`Approved` (DWBI-001–020), 5 `Draft`/`Pending` (DWBI-021–025). This is the first DWBI production pass to leave the KA in a mixed-status state; consistent with the existing convention elsewhere in the bank where Draft content coexists alongside Published content across different KAs, just newly present within DWBI's own folder.

**Cross-KA questions in the full DWBI set:** DWBI-024 (→META) and DWBI-025 (→MASTER) are the only two; both new, both correctly DWBI-primary complements to existing MASTER-primary/META-primary questions rather than restatements of them.

### Addendum Summary

The five new questions are factually accurate, non-duplicative against both the existing 20 DWBI questions and the two cross-referenced questions in other KAs, correctly tagged for DAMA/Industry Practice provenance, and calibrated at a difficulty level matching their actual cognitive demand. One candidate gap (MOLAP/ROLAP/HOLAP) was deliberately not produced as a question, on the judgment that the module's own de-emphasis of it as an implementation detail made it lower-value than the five gaps that were closed. No disqualifying issues found at Gate 1 or Gate 2.

**Outcome: 5 questions pass Gate 1 and Gate 2. Gate 3 (Publish/Approve) is intentionally not executed.** `review_status: Draft`, `approval_status: Pending` remain on `DWBI-021.yaml` through `DWBI-025.yaml`, awaiting the user's explicit approval of this Knowledge Area before any status change or progression to the next KA.
