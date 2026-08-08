# Content Quality Audit: DWBI-021 through DWBI-025

**Audit date:** 2026-08-08
**Scope:** The 5 newly authored DWBI questions (DWBI-021–025), each re-examined independently against `question_bank/authoring_guidelines.md`, `difficulty_framework.md`, `metadata_schema.md`, `question_lifecycle.md`, `research/source_map.md`, `research/source_registry.yaml`, the full `knowledge_base/data_warehousing_and_business_intelligence.md` module, all 20 existing DWBI questions, and the two cross-referenced questions (`MASTER-026`, `META-025`).
**Auditor stance:** This is an independent critical pass, not a re-statement of the production-time self-review already recorded in `reviews/questions_data_warehousing_and_business_intelligence_review.md`'s addendum. That addendum passed all 5 questions at Gate 1/Gate 2. This audit re-opens that judgment and found real defects the production-time review missed — see Biggest Recurring Problems, below. No question file has been modified as part of this audit.

## Summary

| Metric | Value |
|---|---|
| Total audited | 5 |
| STRONG | 1 |
| NEEDS_IMPROVEMENT | 4 |
| REPLACE | 0 |

**Readiness verdict: DWBI is NOT yet ready to serve as production-standard content in its current state.** None of the 5 defects found rise to REPLACE — all are precise, targeted, single-question fixes, not fundamental redesigns — but 4 of 5 questions have a concrete, named defect that should be corrected before Approval/Publish. All 5 questions remain `review_status: Draft`, `approval_status: Pending`, which is the correct state for this finding (no premature publish occurred).

---

## Per-Question Findings

### DWBI-021 — Data Vault Hub/Link/Satellite structure

**Classification: NEEDS_IMPROVEMENT**

1. **DAMA conceptual accuracy:** Correct. Matches the module's Data Vault Approach description (Hubs = business keys, Links = relationships between hubs, Satellites = descriptive time-stamped attributes) exactly.
2. **Source traceability:** Correct. References `knowledge_base/data_warehousing_and_business_intelligence.md, Section 4, DW/BI Architecture Approaches (Data Vault Approach)` — verified to exist and match.
3. **Scenario realism:** N/A (Multiple Choice, no scenario — appropriate for Beginner recall).
4. **Reasoning vs. decoration:** N/A — a direct recall question, correctly typed as Multiple Choice rather than dressed up as a fake scenario.
5. **Distractor quality:** Good in concept — each distractor pulls a real triad of terms from a genuinely adjacent context (Kimball's Fact/Dimension/Bridge, DW/BI pipeline layer names, Governance's Policy/Standard/Procedure hierarchy), consistent with `authoring_guidelines.md`'s Distractor Design priority order (adjacent-topic and adjacent-KA terms).
6. **Explanation quality:** Complete — covers correct-answer reasoning and one distinct reason per distractor.
7. **Difficulty accuracy:** Appropriate. Beginner/Remember correctly matches "recall of a single, isolated fact... distractors are clearly different concepts, not fine-grained misreadings" per `difficulty_framework.md`.
8. **Bloom's-level accuracy:** Correct (Remember).
9. **Cross-KA relevance:** Correctly single-KA; no forced cross-referencing.
10. **Duplicate/redundancy risk:** None found. Checked against DWBI-008 (Kimball identification, Data Vault appears only as a wrong option) and DWBI-016 (Advanced strategic hybrid-architecture choice) — neither tests Data Vault's internal structure directly; DWBI-021 is the only question in the set that does.
11. **Metadata correctness:** Complete and correctly typed. `source_confidence: Medium` is appropriately conservative for `[DAMA + Industry Practice]`-tagged, named-author (Linstedt) content, consistent with the Medium confidence already used on sibling named-author questions DWBI-008 and DWBI-016.
12. **CDMP exam usefulness:** High — closes a real, previously-untested gap. "Data Vault (Hub/Link/Satellite)" is explicitly named in the module's own Section 8 "Important definitions" exam-focus list, and until this question, nothing in the bank tested it as a primary subject (only as a label in DWBI-008/016).

**The problem:** Option B is dramatically longer than options A, C, and D:
- A) "Fact, Dimension, Bridge" (3 words)
- B) "Hub (business keys), Link (relationships between hubs), Satellite (descriptive, time-stamped attributes)" (14 words, three embedded parenthetical definitions)
- C) "Staging, Presentation, Semantic" (3 words)
- D) "Policy, Standard, Procedure" (3 words)

This directly violates `authoring_guidelines.md`'s Stem Writing Rule: *"Keep all options grammatically parallel and similar in length — an option that's conspicuously longer/more detailed than the others is a well-documented 'correct answer' tell."* A test-savvy learner can identify B as correct purely from its length and level of detail, without knowing any Data Vault content — this undermines the question's validity as a knowledge check.

**Recommended correction:** Shorten option B to match the terse, unglossed format of A/C/D — e.g., `"B) Hub, Link, Satellite"` — and rely on the `explanation` field (which already covers what each term means) to carry the definitional detail. Do not add matching parentheticals to A/C/D instead; that would make an already-long option set even longer without adding pedagogical value.

---

### DWBI-022 — OLAP operation categorization (Slice/Dice/Drill-down/Roll-up)

**Classification: NEEDS_IMPROVEMENT**

1. **DAMA conceptual accuracy:** Correct at the level of individual operation definitions — all four match the module's `[Industry Practice]`-tagged definitions verbatim in substance. The specific *categorization* (slice/dice = same-level cross-section selection; drill-down/roll-up = level-of-aggregation change) is not a verbatim module statement — it is this author's own defensible synthesis built from the four given definitions. This is correctly disclosed via `source_confidence: Medium` rather than `High`, and the categorization itself is sound (slicing fixes one dimension's value without changing aggregation level; dicing selects a sub-cube across multiple dimensions, also without changing aggregation level; drill-down/roll-up explicitly traverse a dimension hierarchy, which does change aggregation level) — standard, non-controversial OLAP framing, not a fabrication.
2. **Source traceability:** Correct — `Section 4, OLAP and Multidimensional Analysis (Slice / Dice / Drill-down / Roll-up)`.
3. **Scenario realism:** Thin. "An analyst is working with a Sales OLAP cube" names a plausible business context but does nothing else — no company, no consequence, no decision point.
4. **Reasoning vs. decoration — the problem:** The scenario wrapper is decorative, not load-bearing. The question would be identical in substance without the "Sales OLAP cube" framing — it is fundamentally a categorization exercise over four fixed definitions, not application of a concept to a described business situation with a tradeoff or decision, which is `difficulty_framework.md`'s defining test for Advanced ("Applying a concept to a novel, described business situation and reasoning about a tradeoff or decision, not just classifying a fact... Typical question characteristics: A short original scenario requiring the learner to identify the correct... decision for a described situation"). What this question actually asks — group four related terms by a shared underlying property — is a closer match to Intermediate's own definition: *"Understanding relationships between two related concepts, or correctly classifying an example against a defined framework... requires applying a definition, not just stating it."* `difficulty_framework.md`'s own guidance is explicit on this exact situation: *"If the honest answer doesn't match the intended level, the stem needs rework, not just a metadata relabel."*
5. **Distractor quality:** Genuinely strong — using slice and dice (the two real "wrong" operations) as distractors, rather than made-up terms, forces authentic categorization rather than elimination-by-irrelevance. This part of the design is a real strength, independent of the difficulty-calibration problem.
6. **Explanation quality:** Complete and clear on why B/D are correct and A/C are not.
7. **Difficulty accuracy — the problem:** Miscalibrated. Advanced/80-second estimated solving time overstates the actual cognitive demand; see Reasoning vs. Decoration above.
8. **Bloom's-level accuracy:** Follows from the same issue — "Analyze" is arguable but "Understand" (classifying against a defined framework) is the more honest fit given the actual stem has no situational reasoning to perform, only categorization.
9. **Cross-KA relevance:** Correctly single-KA.
10. **Duplicate/redundancy risk:** None found. Checked against DWBI-005 (bare OLAP definition) and DWBI-010 (OLAP vs. OLTP workload scenario) — distinct cognitive task in both cases.
11. **Metadata correctness:** Otherwise complete; `estimated_solving_time: 80` should move to the Intermediate band (35–50s) if difficulty is recalibrated per the recommendation below.
12. **CDMP exam usefulness:** Good content value regardless of the difficulty question — OLAP operation vocabulary is real, testable, previously-uncovered ground. The value is in the content, not the current difficulty label.

**Recommended correction:** Recalibrate `difficulty` to `"Intermediate"` and `blooms_level` to `"Understand"` (this content is a near-exact match for Intermediate's own definition), and reduce `estimated_solving_time` from 80 to ~45 seconds to match the Intermediate band. Do not discard the question — the categorization content itself is sound and the distractor design is genuinely good; only the difficulty/Bloom's metadata (and the resulting difficulty-tier count) needs to change. Alternative (not recommended over the simpler fix): rework the stem to introduce an actual decision or consequence tied to choosing the right operation, which would legitimately earn Advanced — but this is more invasive than necessary for content this fundamentally sound.

---

### DWBI-023 — Scorecard vs. Dashboard distinction

**Classification: STRONG**

1. **DAMA conceptual accuracy:** Correct — matches the module's Scorecard definition exactly ("similar to a dashboard but explicitly organized around performance against defined targets or goals... the target/threshold context is the defining difference from a plain dashboard").
2. **Source traceability:** Correct — `Section 4, BI Delivery Mechanisms`.
3. **Scenario realism:** Good — a concrete, plausible BI-tool behavior (region-level sales vs. board-approved targets with a red/green indicator) rather than an abstract restatement of the definition.
4. **Reasoning vs. decoration:** Genuine — the learner must recognize which single feature (target-comparison structure) distinguishes the described display from an otherwise-similar Dashboard, not merely recall "what is a scorecard."
5. **Distractor quality:** Solid. Dashboard is the load-bearing near-miss distractor (the actual confusable pair the module documents); standard report and ad hoc tool are clearly-wrong-but-plausible BI-mechanism-category distractors, not strawmen.
6. **Explanation quality:** Complete, covers correct reasoning and each distractor.
7. **Difficulty accuracy:** Appropriate — Intermediate/Understand matches "frequently confused concepts... requires applying a definition, not just stating it" precisely.
8. **Bloom's-level accuracy:** Correct.
9. **Cross-KA relevance:** Correctly single-KA.
10. **Duplicate/redundancy risk:** None found. Checked against DWBI-012 (BI Delivery Mechanisms, Multiple Select) — DWBI-012 does not even include "scorecard" as an answer option (its correct set is report/dashboard/ad hoc); its task is "which of these are BI delivery mechanisms at all" (inclusion), not "which specific mechanism is this" (discrimination between two similar ones). Distinct cognitive task, no overlap.
11. **Metadata correctness:** Complete. One minor, non-disqualifying observation: `source_confidence: High` is a defensible but slightly generous call — the module's dual `[DAMA + Industry Practice]` tag on Scorecard is structurally similar to the tag on DWBI-008/DWBI-016's named-author content, both of which use `Medium`. The difference is that the module states Scorecard's distinguishing feature plainly, without the explicit "exact framing varies across practitioner sources" hedge it applies to Inmon/Kimball/Data Vault — so `High` is a reasonable reading of the schema, not an error, but a reviewer could reasonably argue for `Medium` on consistency grounds. Not severe enough to change the classification.
12. **CDMP exam usefulness:** High — this is exactly the "frequently confused concepts" style question the exam favors, discovered as a real, previously-uncovered gap (DWBI-012's Multiple Select didn't cover it).

---

### DWBI-024 — Semantic layer sourced from Business Glossary (complement to META-025)

**Classification: NEEDS_IMPROVEMENT**

1. **DAMA conceptual accuracy:** Correct — matches the module's framing of the semantic layer as "directly extending the Business Glossary and Business Metadata concepts," and correctly avoids restating META-025's own already-established comprehension-failure scenario.
2. **Source traceability:** Reasonable — cites both `data_warehousing_and_business_intelligence.md, Section 4, ETL and ELT (Semantic Layer)` and `metadata_management.md, Section 3, Business Metadata; Section 4, Key Metadata Concepts (Business Glossary)`. The DWBI-side citation was directly re-verified against the module in this audit; the META-side citation was not independently re-verified against a fresh read of `metadata_management.md` in this pass (relies on recall from earlier in the session) — flagged here as a should-verify item before Approval, not a confirmed error.
3. **Scenario realism — the problem:** The stem opens with "A DW/BI team is designing the semantic layer for a new self-service BI rollout" — no industry, no company type, no concrete organizational context. This falls short in two ways: (a) it does not follow the task's own explicit instruction to use a named industry (government, telecom, banking, healthcare, retail, or enterprise data platforms — anything other than insurance, which META-025 and MASTER-026 both already use) when authoring the cross-KA complements; (b) it is noticeably thinner than the concreteness standard set by every other Scenario-Based question in the DWBI set, all of which name a specific company type or context (DWBI-006's regional sales team, DWBI-010's e-commerce checkout system, DWBI-016's financial services firm, DWBI-025's telecom company).
4. **Reasoning vs. decoration:** The underlying cognitive task is genuine — a proactive build-vs.-reuse-governed-metadata decision, distinct from META-025's reactive diagnosis — but the missing industry grounding makes it read closer to an abstracted policy statement than a fully realized scenario.
5. **Distractor quality:** Good — each option represents a real, documented failure pattern (independently reinventing labels, skipping business-friendly labels entirely, over-correcting into full manual re-documentation) rather than an arbitrary wrong answer.
6. **Explanation quality:** Complete and clear.
7. **Difficulty accuracy:** Reasonable — Intermediate/Apply correctly sits between Beginner recall and Advanced multi-factor tradeoff reasoning; applying the reuse-over-reinvention principle to a new situation is a legitimate Apply-level task even with the scenario's current thinness.
8. **Bloom's-level accuracy:** Correct.
9. **Cross-KA relevance:** Correctly DWBI-primary, META secondary. Re-verified fresh against META-025's full text in this audit: the two are genuinely non-duplicative — different narrative moment (proactive design decision vs. reactive diagnosis of an observed comprehension failure), different answer pattern, no shared stem language. The cross-KA relationship requirement is satisfied.
10. **Duplicate/redundancy risk:** None found against DWBI-013 (generic "what problem does a semantic layer solve" — definitional) or DWBI-015 (self-service BI governance risk — diagnoses fragmentation *after* the fact, a different failure mode than DWBI-024's proactive sourcing decision).
11. **Metadata correctness:** Complete; `industry_practice_concept: "Semantic Layer..."` / `dama_concept: null` correctly mirrors DWBI-013's own tagging convention for the same underlying concept.
12. **CDMP exam usefulness:** Moderate — the underlying relationship is genuinely valuable and exam-relevant, but the thin scenario setting undersells it relative to what the content deserves.

**Recommended correction:** Add a specific named industry/organization type to the stem's opening sentence — e.g., *"A retail enterprise's DW/BI team is designing the semantic layer for a new self-service BI rollout"* or *"A government agency's DW/BI team..."* — matching the concreteness standard already established across the rest of the DWBI set and the task's explicit instruction to differentiate the industry framing from META-025/MASTER-026's insurance setting. No other change is needed; the decision logic, options, and explanation are otherwise sound.

---

### DWBI-025 — Conformed dimension broken by inconsistent MDM sourcing (complement to MASTER-026)

**Classification: NEEDS_IMPROVEMENT**

1. **DAMA conceptual accuracy:** Correct and well-grounded — directly reflects the module's own cross-reference language ("Conformed dimensions... almost always sourced from golden records produced by MDM... not an independently reconciled copy of it," Section 4, Relationships With Other DAMA Knowledge Areas), re-verified fresh in this audit.
2. **Source traceability:** Correct — cites `data_warehousing_and_business_intelligence.md, Section 4, DW/BI Architecture Approaches (Kimball Approach)` and `reference_and_master_data.md, Section 5, Data Engineer Perspective (Data warehouses)`, matching the same MASTER-side citation MASTER-026 itself uses.
3. **Scenario realism:** Good — a concrete, named-industry (telecom) two-mart scenario with a specific, diagnosable symptom (inconsistent join counts), meeting the task's instruction to differentiate industry framing from MASTER-026's insurance setting.
4. **Reasoning vs. decoration:** Genuine — this is the strongest-designed reasoning task of the five. The learner must recognize that two dimensions sharing a name are not automatically "conformed" in the DAMA sense, and diagnose *why* an observed symptom occurred, not just recall a definition.
5. **Distractor quality:** Strong. B is a plausible absolute-overgeneralization distractor (echoing the module's own "no approach is unconditionally X" Exam Trap pattern); C is a genuinely tempting backwards-remediation distractor a rushed reader might pick; D is a defeatist "nothing can be done" distractor that tests whether the learner understands conformance as an enforced governance discipline rather than an automatic byproduct.
6. **Explanation quality:** Complete, covers the correct reasoning and each distractor individually.
7. **Difficulty accuracy:** Well-justified — Advanced/Analyze is the best-earned difficulty label of the five new questions; this genuinely requires multi-entity diagnostic reasoning, not classification against a fixed framework.
8. **Bloom's-level accuracy:** Correct.
9. **Cross-KA relevance:** Correctly DWBI-primary, MASTER secondary. Re-verified fresh against MASTER-026's full text: genuinely distinct — MASTER-026 is a build-time sourcing *choice* among four options (insurance, building a new dimension); DWBI-025 is a diagnostic *analysis* of a symptom in an existing warehouse (telecom, two already-built dimensions). Different narrative moment, different answer pattern, no shared stem language or reasoning chain. The cross-KA requirement is satisfied.
10. **Duplicate/redundancy risk:** None found against DWBI-006 (independent vs. dependent *data mart* — a whole-mart bypass, a different failure mode) or DWBI-011 (conformed dimension's generic purpose — bare definition, no diagnostic element).
11. **Metadata correctness — the problem:** Option A is roughly 2.5–3x longer than options B, C, and D, because it embeds its own justification clause directly in the answer-choice text:
    - A) "The Support mart's Customer dimension isn't actually sourced from the golden record, so despite sharing the same name, it isn't a true conformed dimension — conformance requires marts to share the same governed entity, not just similarly-named tables" (~38 words, includes an em-dash-introduced justification clause)
    - B) "Kimball-style warehouses cannot support more than one data mart referencing the same dimension" (~14 words)
    - C) "The Billing mart should be rebuilt to match Support's extraction method instead" (~13 words)
    - D) "This is expected and unavoidable whenever two marts both reference a Customer dimension" (~14 words)

    This is the same class of defect as DWBI-021 (a "correct answer" length tell per `authoring_guidelines.md`'s Stem Writing Rules), though less severe in ratio — it is still a real, fixable problem, not a disqualifying one, since the underlying diagnostic content is otherwise the strongest in the batch.
12. **CDMP exam usefulness:** High — once trimmed, this is the best-designed question of the five: realistic, genuinely diagnostic, well-differentiated from its MASTER-026 counterpart, and testing a high-value relationship explicitly named in the module's own cross-reference section.

**Recommended correction:** Trim option A to remove the embedded justification clause, moving that reasoning into the `explanation` field (which already restates substantially the same point). Suggested replacement: `"A) The Support mart's Customer dimension isn't actually sourced from the golden record, so it isn't a true conformed dimension despite the shared name"` — still slightly longer than B/C/D (unavoidable given it must name the specific cause), but no longer conspicuously so.

---

## Cross-Cutting Assessments

### Scenario Quality Assessment

Three of the five new questions (DWBI-023, DWBI-025, and — partially — DWBI-022) build scenarios that genuinely force reasoning rather than decorate a definition, consistent with the standard set by the strongest existing DWBI questions (DWBI-006, DWBI-015, DWBI-016). Two show a real, specific weakness:
- DWBI-022's scenario is present but non-load-bearing — the question is a categorization exercise wearing a thin scenario costume, not a situation requiring reasoning about the situation itself.
- DWBI-024's scenario is load-bearing in terms of cognitive task but under-specified in setting — it lacks the named-industry concreteness the task explicitly asked for and the rest of the set consistently delivers.

Neither is a "definition wrapped in a company story" in the disqualifying sense the task warned against (both require genuine reasoning, not just recall), but both fall short of the DWBI set's own established bar for scenario craftsmanship.

### Source Quality Assessment

All five questions are correctly sourced to real, verified sections of `knowledge_base/data_warehousing_and_business_intelligence.md`; none reproduce copyrighted DMBOK2 text; all correctly separate `[DAMA]`-tagged content from `[Industry Practice]`-tagged content (Data Vault, OLAP operations, and the Semantic Layer are all correctly `industry_practice_concept`-tagged rather than misrepresented as core DAMA doctrine, per `research/source_map.md`'s priority rules). No unregistered source was cited as authoritative — the only sources drawn on (`dmbok2-2nd-ed` via the Approved module, plus the DWBI module's own already-established `[Industry Practice]` hedges on Kimball/Data Vault/OLAP operations) are already properly registered in `research/source_registry.yaml`. One traceability item — DWBI-024's `metadata_management.md` section citation — was not independently re-verified in this pass and should be spot-checked before Approval, though there is no specific reason to believe it is wrong.

### Cross-KA Assessment

Both mandatory cross-KA complements (DWBI-024 → META-025, DWBI-025 → MASTER-026) were independently re-verified in this audit against fresh, full reads of both target questions. Both are genuinely DWBI-primary, non-duplicative in stem, cognitive task, scenario structure, answer pattern, and reasoning — they test the same underlying relationship from the opposite side, exactly as instructed, not restatements. DWBI-025's execution of this requirement is notably stronger than DWBI-024's, primarily because of the scenario-concreteness gap noted above.

### Biggest Recurring Problems

1. **Correct-answer length tell (2 of 5 questions: DWBI-021, DWBI-025).** In both cases, the author embedded the correct answer's justification directly in the `answer_choices` text rather than deferring it to `explanation`, producing an option conspicuously longer than its distractors — a specifically named anti-pattern in `authoring_guidelines.md`. This is the single most consistent, most mechanically fixable defect found in this batch, and worth calling out as a pattern to watch for in future authoring passes (ETH/DOC and beyond), not just a one-off slip.
2. **Scenario concreteness gap under thin/no industry framing (1 of 5: DWBI-024, partially DWBI-022).** Where a scenario should be doing real work (grounding a decision in a specific organizational context), a generic "A DW/BI team..." opener undersells otherwise-sound content.
3. **Decorative-scenario / difficulty-inflation risk (1 of 5: DWBI-022).** A single instance, but worth flagging because it's exactly the failure mode the task asked to specifically screen for (criterion 4) — a scenario wrapper that doesn't change the underlying cognitive task from what a plain definitional question would already test.

None of these three problems is a factual/DAMA-accuracy defect — all five questions are correct in what they teach. The defects are entirely in execution polish (option-length parallelism, scenario concreteness, difficulty calibration), which is precisely why none rise to REPLACE.

### Strongest Example

**DWBI-025.** The best-executed reasoning task in the batch: a concrete, differentiated-industry scenario; a genuine diagnostic cognitive task (not decorated recall); well-grounded, non-strawman distractors; the most convincingly earned Advanced/Analyze calibration of the five; and the cleanest, most rigorously verified non-duplication against its MASTER-026 counterpart. Its only flaw (the length tell on option A) is a small, mechanical fix, not a design problem.

### Weakest Example

**DWBI-022.** Not weak in content — the individual OLAP operation definitions and the categorization distractor design are both sound — but weakest in calibration: the difficulty/Bloom's-level label (Advanced/Analyze) does not match what the question actually asks the learner to do (Intermediate/Understand-level categorization dressed in a thin scenario wrapper). This is a metadata-and-stem-honesty problem, not a content-quality problem, but it's the most conceptually significant finding in this audit because it's exactly the "decorated definition" failure mode the task asked to specifically guard against.

---

## Overall Readiness Verdict

**DWBI is not yet ready to serve as production-standard content.** 4 of 5 new questions need a specific, named, single-question correction before this batch should proceed to Gate 3/Approval — none require a full rewrite, and the underlying DAMA content, sourcing discipline, and cross-KA design are all sound across all five. The recommended corrections are:

| Question | Fix | Effort |
|---|---|---|
| DWBI-021 | Shorten option B to remove length tell | Trivial |
| DWBI-022 | Recalibrate difficulty to Intermediate/Understand, solving time to ~45s | Trivial (metadata only) |
| DWBI-023 | None required (optional: reconsider source_confidence to Medium for consistency) | — |
| DWBI-024 | Add a named industry/organization to the stem's opening sentence | Small |
| DWBI-025 | Trim option A to remove length tell | Trivial |

No question in this batch is authored on a false factual premise, and no cross-KA duplication was found against MASTER-026 or META-025. This audit deliberately did not apply any of the recommended corrections, per the task's explicit instruction to report only.
