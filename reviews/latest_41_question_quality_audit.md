# Content Quality Audit: The Latest 41 New Questions (Six-KA Expansion)

**Audit date:** 2026-08-08
**Auditor:** Claude (CDMP Mentor), acting as an independent critical reviewer of its own prior authoring work
**Scope:** The 41 questions added in the six-KA expansion batch — `GOV-021`–`028`, `MODEL-021`–`027`, `QUAL-021`–`027`, `META-021`–`026`, `ARCH-021`–`026`, `MASTER-021`–`027`. The original 266 questions and all six `knowledge_base/` modules were **not** re-litigated here except as ground truth to check the 41 against.
**Method:** Every one of the 41 files was re-read fresh from disk (not from memory of authoring them), cross-checked against the exact `knowledge_base/*.md` sections cited in `references`, and — where a subtopic looked close to existing content — cross-checked directly against the specific existing sibling question(s) rather than just the topic/keyword summary used during original authoring. This last step is what surfaced this audit's most important finding (see §REPLACE below). No file was modified.

---

## Summary Counts

| | Count |
|---|---|
| **Total audited** | **41** |
| **STRONG** | **36** (88%) |
| **NEEDS_IMPROVEMENT** | **4** (10%) |
| **REPLACE** | **1** (2%) |

Per KA: GOV 5 STRONG / 3 NEEDS_IMPROVEMENT / 0 REPLACE (8) · MODEL 7/0/0 (7) · QUAL 6/0/1 (7) · META 6/0/0 (6) · ARCH 6/0/0 (6) · MASTER 6/1/0 (7).

---

## Full Classification

### GOV (8 audited)

| ID | Class | Notes |
|---|---|---|
| GOV-021 | **NEEDS_IMPROVEMENT** | See below. |
| GOV-022 | STRONG | Clean Decentralized/Federated classification; Registry-style distractor correctly pulls a genuine cross-KA confusion (MASTER). |
| GOV-023 | **NEEDS_IMPROVEMENT** | See below. |
| GOV-024 | **NEEDS_IMPROVEMENT** | See below. |
| GOV-025 | STRONG | GDPR scenario. All three distractors map to real, documented Common Mistakes (engineers-as-de-facto-owners; governance-as-one-time-project). |
| GOV-026 | STRONG | Cross-agency government scenario. Distractor A directly reuses the documented "governance = IT function" trap. |
| GOV-027 | STRONG | Multiple Select; both distractors are genuine, non-obvious misconceptions ("more review = more effective governance"), not strawmen. |
| GOV-028 | STRONG | Minor note: distractor D (Segregation of Duties) is the weakest of the three — plausible but less tightly grounded than A/C. Not blocking. |

**GOV-021 — NEEDS_IMPROVEMENT.** Tests the Guideline-vs-Standard distinction at **Beginner** difficulty with `source_confidence: Medium`. The source module itself only hedges this content ("*Some* frameworks add a fourth tier... DMBOK2 references this tier *in places*") — it does not confirm DMBOK2 2nd Ed. formally enumerates "Guideline" as a named artifact. The stem and explanation correctly preserve this hedge in their own wording, so no answer option is made incorrectly "arguably correct" by the ambiguity (Standard 1 is technically satisfied) — but presenting genuinely uncertain source attribution at Beginner level, where a learner reasonably assumes "settled fact," is a risk. **Recommended correction:** before Approval, verify against the physical `dmbok2-2nd-ed` copy whether the 2nd Edition explicitly names a "Guideline" tier. If confirmed, keep as-is. If not, either reclassify to Intermediate (framing it as broader governance-framework literacy rather than a DMBOK2-specific fact) or rework the stem to foreground the uncertainty explicitly.

**GOV-023 — NEEDS_IMPROVEMENT.** Labeled Intermediate/`Understand`, but the stem is a direct, undecorated restatement of a relationship the source module states almost verbatim ("Governance decides what quality standards should be; Data Quality Management measures and improves against those standards") — there is no described situation requiring the learner to *apply* the distinction, only to recall it. This is Beginner/`Remember`-shaped content mislabeled. **Recommended correction:** either reclassify to Beginner/`Remember`, or rewrite as a short scenario (e.g., "A Data Steward sets a 95% completeness threshold approved by the Data Owner; a Data Engineer builds the validation job enforcing it. Which KA governs the threshold decision, and which governs the enforcement mechanism?") to genuinely earn the Intermediate/`Apply` label.

**GOV-024 — NEEDS_IMPROVEMENT.** All three distractors (Records Retention Schedule, Data Sharing Agreement, RPO) are *correct concepts from other Knowledge Areas* but none is a genuinely confusable artifact for "Business Glossary" specifically — they read as topically-adjacent filler rather than plausible misconceptions a learner might actually hold. This falls short of the Intermediate-tier standard in `difficulty_framework.md` ("at least one distractor is the other half of a commonly-confused pair") and `authoring_guidelines.md`'s Distractor Design priority order. **Recommended correction:** replace at least one distractor with a genuinely confusable artifact — e.g., "A Data Dictionary" or "A Metadata Repository" or "A Data Catalog" — something a learner could plausibly conflate with a governed Business Glossary specifically.

### MODEL (7 audited)

| ID | Class | Notes |
|---|---|---|
| MODEL-021 | STRONG | Natural/Surrogate Key, telecom. Distractor C directly reuses the module's own documented Exam Trap. |
| MODEL-022 | STRONG | Textbook 1NF/2NF discrimination via a concrete composite-key example. |
| MODEL-023 | STRONG | Naming-standards/model-governance, insurance. Distractor D (Uniqueness) is a well-chosen near-miss. |
| MODEL-024 | STRONG | Kimball attribution; matches the established, previously-praised provenance-question pattern from the original set. |
| MODEL-025 | STRONG | Minor note: distractor D (backup failure) is the weakest of three; B and C are strong, well-grounded near-misses. Not blocking. |
| MODEL-026 | STRONG | Minor note: distractor D (Storage and Operations) is the weakest; A and C are strong, realistic engineer rationalizations. Not blocking. |
| MODEL-027 | STRONG | One of the strongest in the batch — all three distractors are genuinely plausible, internally coherent wrong strategies (force uniformity; patch only the reporting layer; treat as pure integration). |

No REPLACE or NEEDS_IMPROVEMENT in this set. Checked MODEL-023, MODEL-025, MODEL-026 against the existing set's closest neighbors (MODEL-011 Modeling-vs-Architecture, MODEL-006/010 Logical-vs-Physical) — no overlap found; all seven test genuinely new territory.

### QUAL (7 audited)

| ID | Class | Notes |
|---|---|---|
| QUAL-021 | STRONG | Clean, textbook Validity question. |
| QUAL-022 | **REPLACE** | See below — the single most important finding of this audit. |
| QUAL-023 | STRONG | Distractor A directly reuses the module's own documented Common Mistake #1 ("treating quality as only a technical issue"). |
| QUAL-024 | STRONG | One of the best-constructed Intermediate questions in the batch — all three distractors are sibling dimensions from the module's own documented Consistency-vs-Integrity Exam Trap pair. |
| QUAL-025 | STRONG | Data Contract / shift-left, well-grounded in the module's explicit cost-of-late-detection framing. |
| QUAL-026 | STRONG | Cross-KA QUAL/BIGDATA, well-reasoned. |
| QUAL-027 | STRONG | Clean Multiple Select; both distractors are genuine sibling-dimension near-misses (Consistency, Uniqueness). |

**QUAL-022 — REPLACE.** This question is a **near-duplicate of the existing `QUAL-010`** (still in the bank, `Draft`, untouched). Side-by-side: both stems ask, in near-identical wording, "what happens immediately after identifying a quality issue" in the DQM lifecycle; both offer the same four answer concepts (deploy a monitoring dashboard / analyze root causes / cleanse the data / notify Governance and stop); both have the same correct answer (root cause analysis) with the same underlying reasoning; both cite the identical `knowledge_base/data_quality.md, Section 4` reference; both are Intermediate/`Understand`. This does **not** qualify for the "deliberately targets a different Bloom's level/type/difficulty" exception in `question_quality_standards.md` Standard 11 — every one of those axes matches.
**Root cause:** the original authoring-time duplication check (documented in the `reviews/questions_data_quality_review.md` addendum) was performed at the aggregate topic/subtopic/keyword level, not by reading `QUAL-010`'s actual stem before drafting `QUAL-022` in the same "DQM Lifecycle" subtopic — a process gap, not a one-off content slip, and worth flagging for future batches specifically.
**Recommended correction:** retire `QUAL-022` as currently authored. If the DQM-lifecycle-ordering territory still merits a second question, author a genuinely distinct one — e.g., a question requiring the learner to sequence *multiple* lifecycle steps at once, or one testing a different transition (such as "what happens when Monitoring detects a regression — does it re-enter at Define Requirements or at Identify Issues?") — rather than repeating the "issue identified → what's next" framing `QUAL-010` already owns.

### META (6 audited)

| ID | Class | Notes |
|---|---|---|
| META-021 | STRONG | Verified distinct from the existing `MASTER-015` (same underlying trap, genuinely different distractor set and framing — legitimate two-sided reinforcement, not duplication). |
| META-022 | STRONG | Clean definitional recall, correctly distinguished from Metadata Repository. |
| META-023 | STRONG | Minor note: distractor C ("government agencies inherently unable...") is a weak, ungrounded strawman relative to A and D, which are both reasonably plausible. Not blocking on its own. |
| META-024 | STRONG | Cross-KA META/SEC, well-grounded in the module's own explicit cross-reference. |
| META-025 | STRONG | Minor note: distractor B ("increase storage capacity") is an ungrounded filler relative to C and D. Not blocking on its own. |
| META-026 | STRONG | Clean, well-reasoned. |

No REPLACE or NEEDS_IMPROVEMENT. The two footnoted single-weak-distractor cases (META-023, META-025) did not individually cross the bar for NEEDS_IMPROVEMENT (a majority of a question's distractors would need to be ungrounded), but both are named in the recurring-problems section below since the pattern repeats often enough to be worth a future pass.

### ARCH (6 audited)

| ID | Class | Notes |
|---|---|---|
| ARCH-021 | STRONG | Zachman attribution; correctly extends the established TOGAF-attribution pattern (ARCH-005) to a previously-untested framework. |
| ARCH-022 | STRONG | Clean Logical-layer discrimination against its Conceptual/Physical/Database-Design siblings. |
| ARCH-023 | STRONG | Verified distinct from the existing `ARCH-010` (artifacts-vs-standards, single-KA) — this one is a genuinely new cross-KA (ARCH-vs-GOV Standards) comparison. |
| ARCH-024 | STRONG | Data Mesh attribution; parallel, non-duplicative extension of the same pattern as ARCH-021. |
| ARCH-025 | STRONG | Minor note: distractor C ("required by DAMA to maximize engineering autonomy") is not grounded in any real DAMA claim and is the weakest of the three; A and D are well-grounded. Not blocking. |
| ARCH-026 | STRONG | One of the strongest in the batch — all three distractors are realistic, internally coherent wrong sequencing choices. |

No REPLACE or NEEDS_IMPROVEMENT.

### MASTER (7 audited)

| ID | Class | Notes |
|---|---|---|
| MASTER-021 | **NEEDS_IMPROVEMENT** | See below. |
| MASTER-022 | STRONG | Correctly calibrated Intermediate; strong distractor set. |
| MASTER-023 | STRONG | Hierarchies — fills a real, previously-untested gap; all three distractors well-grounded. |
| MASTER-024 | STRONG | Minor note: distractor D (Data Validation) is the weakest of three; A and C are strong. Not blocking. |
| MASTER-025 | STRONG | Beginner-appropriate; obvious-by-design distractors are correct for this tier per `difficulty_framework.md`. |
| MASTER-026 | STRONG | All three distractors are genuinely plausible suboptimal real decisions. |
| MASTER-027 | STRONG | One of the strongest in the batch — a genuine root-cause diagnosis question with three well-grounded, internally coherent wrong diagnoses. |

**MASTER-021 — NEEDS_IMPROVEMENT.** Labeled **Beginner/`Remember`**, but the question presents a full behavioral description and requires the learner to discriminate Consolidation from three similarly-described sibling styles (Registry, Coexistence, Centralized) — the *exact same cognitive task* as the existing `MASTER-008` (Registry) and this batch's own `MASTER-022` (Centralized), both correctly labeled **Intermediate/`Understand`**. This is an internally inconsistent difficulty assignment across three structurally identical questions authored in the same batch. **Recommended correction:** reclassify `MASTER-021` to Intermediate/`Understand`, matching `MASTER-008` and `MASTER-022`'s precedent for the identical question shape.

---

## Scenario Quality Assessment

20 of the 41 new questions are `Scenario-Based`. The large majority (≈18 of 20) genuinely require applying a principle to a described situation to reach the answer — a learner cannot skip the scenario and pattern-match a keyword. `GOV-024` is the one borderline case: the scenario is thinner than the others (a two-sentence definitional-conflict setup that a well-prepared learner can resolve almost immediately), though it's still a legitimate light application, not pure decoration.

**Industry coverage across the 41:** Insurance (7), Telecommunications (4), Retail/e-commerce/cloud platform (4), Banking (3), Government/Public Sector (2). This is a genuine improvement over the original 120, which leaned on banking/healthcare/retail composites without telecom, insurance-as-primary, or dedicated government scenarios in several of these six KAs — matching this task's explicit call for realistic, varied enterprise contexts.

## Source Quality Assessment

Every one of the 41 questions traces to a specific `knowledge_base/*.md` section (cited in `references`); no question cites a page/section number not present in that section's actual heading (spot-checked against the full module text read during this and the prior source-verification phase). No verbatim DMBOK2 or third-party-resource text appears anywhere — every stem, scenario, and explanation is original phrasing. `source_confidence: Medium` is used exactly where the *source module itself* flags uncertainty (`GOV-021`, `ARCH-022`, `MASTER-021`/`022`, `META-025`) — not applied inconsistently. **The third-party practice-question resource (`cdmp-fundamentals-practice-exam-questions`) is not cited anywhere in the 41** — confirmed by grep, consistent with its secondary-only, never-DAMA-authority status.

## Biggest Recurring Problems

1. **Difficulty/Bloom's-level calibration drift on recall-shaped content** — `GOV-023` and `MASTER-021` (and, before its more serious duplication issue was found, `QUAL-022`) are the clearest cases: content that is substantively single-fact recall dressed in an Intermediate/`Understand` or Beginner-inconsistent-with-precedent label. Not a correctness problem, but a genuine calibration gap.
2. **The QUAL-022/QUAL-010 near-duplicate** is the single most serious finding — and, more importantly, it reveals that the original per-KA duplication check (documented in each review addendum as "checked against the existing 20... no near-duplicates found") was performed at too coarse a level (topic/subtopic/keyword aggregation) rather than by reading each candidate sibling question's actual stem. This is a **process** finding, not just a content one, and should change how duplication checks are performed in the next batch: read the specific sibling question(s) in the same subtopic directly, every time, before drafting.
3. **A recurring "filler" distractor pattern** — a minority of Intermediate/Advanced questions include one distractor that is an unrelated, ungrounded technical concept (e.g., RPO, backup failure, storage capacity) rather than a genuine plausible misconception. Individually minor in most cases (1 of 3 distractors, not blocking — `MODEL-025`, `MODEL-026`, `MASTER-024`, `META-023`, `META-025`, `ARCH-025`) but frequent enough across six different KAs to name as a stylistic habit worth tightening in the next batch, even where no single instance crossed the bar into NEEDS_IMPROVEMENT. `GOV-024` is the one case where this pattern was severe enough (affecting all three distractors at once) to cross into NEEDS_IMPROVEMENT outright.

## Strongest Examples

- **`MASTER-027`** (post-merger Data Owner diagnosis) — a genuine root-cause reasoning question with three well-grounded, internally coherent wrong diagnoses (tooling, inevitability, modeling).
- **`MODEL-027`** (insurance Claim conceptual-model reconciliation) — all three distractors are realistic, competent-but-wrong strategies a real team might actually choose.
- **`ARCH-026`** (government digital-platform sequencing) — tests genuine decision-making about deliverable order, not definition recall.
- **`QUAL-024`** (Consistency, telecom) — textbook use of sibling-dimension distractors drawn directly from the module's own documented Exam Trap pair.
- **`GOV-027`** (over-engineering governance, Multiple Select) — both distractors are genuine, non-obvious misconceptions rather than strawmen.

## Weakest Examples

- **`QUAL-022`** — REPLACE; near-duplicate of `QUAL-010`.
- **`GOV-024`** — NEEDS_IMPROVEMENT; all three distractors ungrounded relative to the tested concept.
- **`MASTER-021`** — NEEDS_IMPROVEMENT; difficulty mislabeled relative to its own batch-mate (`MASTER-022`) and the existing `MASTER-008`.
- **`GOV-023`** — NEEDS_IMPROVEMENT; recall-shaped content over-labeled as Intermediate/`Understand`.

## Recommendation: Is This Batch Ready to Serve as the Production Standard?

**Not yet, as-is — but close, and the gap is narrow, not systemic.** 36 of 41 (88%) are genuinely production-quality on every criterion audited and need no rework. The remaining 5 require a small, targeted fix list — not a batch-wide regeneration:

1. Retire/replace `QUAL-022` (near-duplicate).
2. Reclassify `MASTER-021` to Intermediate.
3. Reclassify or rework `GOV-023` (recall vs. Understand mismatch).
4. Strengthen at least one distractor in `GOV-024`.
5. Verify `GOV-021`'s DMBOK2 attribution against the physical source before Approval (or reclassify/reword pending that verification).

None of these five reflect a DAMA-accuracy error — every flagged issue is a calibration, distractor-quality, or duplication defect, not a factually wrong answer. Once addressed, I would consider this batch ready to serve as the production standard for future six-KA-style expansions. I'd also recommend the process fix from Recurring Problem #2 (read sibling stems directly, not just topic/keyword summaries) be applied starting with the next batch, independent of whether these five items are fixed first.

---

## Validation

```
python -m pytest -q
```
Run after this audit; see the accompanying report in the conversation. No `question_bank/`, `knowledge_base/`, `quiz_engine/`, or `packages/` file was modified to produce this audit.

---

## Remediation Results (2026-08-08)

All five items above were remediated. No other question was touched; `knowledge_base/`, `quiz_engine/`, and `packages/` remain untouched. All five files remain `review_status: Draft`, `approval_status: Pending`.

### 1. QUAL-022 — REPLACE, done
Fully replaced (same ID/file, since it was never Published). New subtopic: "DQM lifecycle as a continuous, repeating cycle (Monitoring feeds back)" — tests that a monitoring-detected regression means the lifecycle re-enters at issue-identification/root-cause-analysis, not that the whole program failed. Checked against `QUAL-010` (the original duplicate target), `QUAL-011` (Profiling vs. Monitoring), and `QUAL-017` (monitoring the health of the checks themselves) — genuinely distinct from all three. `QUAL-010` itself was **not modified**.

### 2. GOV-023 — recalibrated
`difficulty: Intermediate → Beginner`, `blooms_level: Understand → Remember`, `estimated_solving_time: 35 → 25`. Learning objective reworded from "State..." to "Recall...". Stem, options, correct answer, and explanation are unchanged — the content was always accurate, only its cognitive-demand labeling was wrong.

### 3. GOV-024 — distractors replaced
Old distractors (Records Retention Schedule, Data Sharing Agreement, RPO) — three correct-but-topically-unrelated artifacts — replaced with **Data Catalog, Metadata Repository, and Data Dictionary**, all genuinely confusable with a Business Glossary per `metadata_management.md`'s own documented Catalog-vs-Repository distinction. Correct answer (B, Business Glossary) is unchanged — the audit found the answer correct, only the distractors weak. Added a `metadata_management.md` reference to ground the new distractor reasoning; `keywords` and `estimated_solving_time` updated accordingly. Checked against `META-009` (the existing Catalog-vs-Repository question) and `GOV-006` (the existing Business-Glossary scenario) — both remain legitimately distinct, not duplicates.

### 4. MASTER-021 — recalibrated
`difficulty: Beginner → Intermediate`, `blooms_level: Remember → Understand`, `estimated_solving_time: 30 → 40`. Learning objective reworded to name the discrimination task explicitly. Stem, options, correct answer, and explanation are unchanged. Now consistent with the identical-shaped `MASTER-008` (Registry) and its own batch-mate `MASTER-022` (Centralized), both already correctly Intermediate.

### 5. GOV-021 — verified against the physical DMBOK2 source and corrected
**Verification performed:** searched the full text of `sources/dmbok2/dama-dmbok-2nd-edition-data-management.pdf` (849 pages) for every occurrence of "Guideline" (32 total), then specifically inspected the Data Governance chapter's artifact/deliverables discussion (pp. ~126–168, located via "Policy"+"Standard"+"Procedure" co-occurrence search). **Finding:** no passage enumerates "Guideline" as a formally defined peer artifact tier alongside Policy/Standard/Procedure. Every occurrence found is either (a) a generic "Implementation Guidelines" chapter-section heading that recurs identically across multiple, unrelated chapters (a structural template item, not a governance-artifact type), or (b) a single casual, undefined "policies and guidelines" pairing in an unrelated activity description, or (c) unrelated external content (OECD guidelines, referenced in the Data Ethics chapter). **No copyrighted text was reproduced anywhere** — only page-range locators and a paraphrased description of what was and wasn't found.
**Correction applied, per the instruction to update only if verification showed insufficient support:** `dama_concept` changed from `"Guideline vs. Standard"` to `null`; `industry_practice_concept` populated with `"Guideline as a non-mandatory governance-artifact tier (general governance-framework convention)"`. Stem and explanation reworded to accurately attribute the Guideline concept as a general governance-framework convention rather than a DMBOK2-defined term, while preserving the correct answer and the underlying mandatory-vs-recommended teaching point (which remains a legitimate, useful distinction on its own merits). Added a `references` entry recording the verification method and locator. `source_confidence` remains `Medium`.
**Important disclosure — not remediated, out of scope:** the existing, unmodified `GOV-008` (`Policy/Standard/Procedure vs. Guideline`, Multiple Select, `source_confidence: High`) makes the same DMBOK2-attribution claim this verification found unsupported. It was **not** in the five-item remediation list and was **not modified**, per the instruction to touch only the five named questions — flagging it here for your awareness and a possible future remediation item.

### Post-remediation validation
- Schema validator across all 307 questions: **0 errors**, all IDs unique.
- `python -m pytest -q`: **63 passed**.
- Duplicate/near-duplicate re-check within the six affected KAs: no new duplicates introduced by these edits. `GOV-024` vs. `GOV-006` (Business Glossary) and `GOV-021` vs. `GOV-008` (Guideline) remain legitimate complementary pairs — different scenarios/distractor sets/question types — not duplicates.
