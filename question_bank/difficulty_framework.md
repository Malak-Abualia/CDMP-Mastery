# Question Bank — Difficulty Framework

## Purpose

Defines the four difficulty levels every question is classified into, how they differ precisely (not just by feel), and how difficulty relates to Bloom's Taxonomy and to actual CDMP exam relevance. Difficulty and Bloom's level are related but not identical — see "Difficulty vs. Bloom's Level" below.

## Sourcing Note

Bloom's Taxonomy (Remember, Understand, Apply, Analyze, Evaluate, Create) is a general educational-assessment framework. **`[Industry Practice]`** — it is not a DAMA/DMBOK2 concept, and using it here does not imply DMBOK2 defines or endorses it. It's adopted in this design because it's the standard, well-understood way to express cognitive demand in an assessment system, exactly the way `data_modeling_and_design.md` adopts Kimball dimensional-modeling vocabulary without claiming DAMA invented it.

## The Four Levels

### Beginner
- **Cognitive demand:** Recall of a single, isolated fact or definition. No application, no comparison, no scenario reasoning required.
- **Bloom's alignment:** Remember, low-end Understand.
- **CDMP relevance:** Matches the bulk of the real Data Management Fundamentals exam, which `research/cdmp_exam_overview.md` describes as "definitional and conceptual... drawn directly from DMBOK2 terminology" rather than scenario-heavy. This is the largest tier by volume in a healthy bank.
- **Typical question characteristics:** "What is the definition of X?" / "Which role is responsible for Y?" — answerable directly from a single `knowledge_base/` Flashcard-equivalent fact, with no synthesis across sections.
- **Distractor sophistication:** Distractors are clearly different concepts, not fine-grained misreadings — the test is "do you know the term," not "can you avoid a trap."
- **Typical types:** Multiple Choice, True/False, Matching (simple term↔definition).

### Intermediate
- **Cognitive demand:** Understanding relationships between two related concepts, or correctly classifying an example against a defined framework.
- **Bloom's alignment:** Understand, low-end Apply.
- **CDMP relevance:** Matches the exam's "frequently confused concepts" style questions — e.g., distinguishing Reference Data from Master Data given a described example, per `reference_and_master_data.md`, Section 3. This tier is where most documented Exam Traps live.
- **Typical question characteristics:** "Given this example, which category does it belong to?" / "What distinguishes X from Y?" — requires applying a definition, not just stating it.
- **Distractor sophistication:** At least one distractor is the *other* half of a commonly-confused pair (e.g., Steward vs. Owner), pulled from the source module's documented Exam Traps or Common Mistakes, per `authoring_guidelines.md`'s Distractor Design method.
- **Typical types:** Multiple Choice, Multiple Select, Matching, Ordering (for a documented lifecycle/hierarchy).

### Advanced
- **Cognitive demand:** Applying a concept to a novel, described business situation and reasoning about a tradeoff or decision, not just classifying a fact.
- **Bloom's alignment:** Apply, Analyze.
- **CDMP relevance:** Matches the "Practitioner-level" scoring band described in `research/cdmp_exam_overview.md` — a candidate scoring for Practitioner (≥70%) rather than just Associate (≥60%) needs to reliably clear this tier, not just Beginner/Intermediate recall.
- **Typical question characteristics:** A short original scenario requiring the learner to identify the correct governance role, MDM implementation style, or architecture decision for a described situation — reasoning from principles, not from memorized fact-lookup.
- **Distractor sophistication:** Distractors represent plausible-but-suboptimal real decisions (e.g., choosing a Centralized MDM style when Registry is actually more appropriate for the described organizational maturity), requiring the learner to weigh tradeoffs, not just recall a definition.
- **Typical types:** Scenario-Based, Multiple Select, Ordering (for a multi-step decision process).

### Expert
- **Cognitive demand:** Synthesizing multiple Knowledge Areas to resolve a multi-part, realistic situation, including recognizing when a described approach is a well-known anti-pattern.
- **Bloom's alignment:** Analyze, Evaluate, occasionally Create (e.g., "propose the most defensible approach given these constraints").
- **CDMP relevance:** Exceeds what a typical Data Management Fundamentals question asks (per `research/cdmp_exam_overview.md`'s "breadth over depth" framing) but is directly useful preparation for CDMP Practitioner and Specialist exams, and for genuine on-the-job mastery — consistent with this project's stated goal of pushing toward Practitioner-level readiness while studying for Fundamentals (`CLAUDE.md`, "My Goals").
- **Typical question characteristics:** A multi-paragraph original scenario spanning two or more Knowledge Areas (e.g., a Master Data initiative that also raises Governance ownership questions and Metadata lineage requirements), evaluated across several sub-questions.
- **Distractor sophistication:** Distractors are internally coherent, well-reasoned *wrong* strategies — the kind a competent-but-incomplete answer would produce — not simple misreadings.
- **Typical types:** Mini Case Study almost exclusively; occasionally a single dense Scenario-Based or Multiple Select question.

## Level Comparison Table

| | Beginner | Intermediate | Advanced | Expert |
|---|---|---|---|---|
| Bloom's level | Remember | Understand / low Apply | Apply / Analyze | Analyze / Evaluate / Create |
| Concepts per question | 1 | 1–2 (a confused pair) | 2–3 (applied to a scenario) | 3+ (cross-KA) |
| Requires a scenario? | No | Sometimes | Usually | Almost always |
| CDMP exam match | Associate-level bulk | Associate + Practitioner | Practitioner-level | Beyond Fundamentals; Practitioner/Specialist prep |
| Typical estimated solving time | 20–35 sec | 35–50 sec | 50–90 sec | 90–180 sec (case study: per sub-question) |
| Typical types | MC, True/False, simple Matching | MC, Multiple Select, Matching, Ordering | Scenario-Based, Multiple Select, Ordering | Mini Case Study |

`estimated_solving_time` ranges above inform the `metadata_schema.md` field of the same name and should be sanity-checked against the real exam's ≈54 sec/question average (`research/cdmp_exam_overview.md`) when assembling Mock Exams — see `architecture.md`, "Mock Exam Engine."

## Difficulty vs. Bloom's Level: Why Both Exist

Difficulty is the learner-facing signal ("how hard is this to get right"); Bloom's level is the assessment-design signal ("what kind of thinking does this require"). They correlate strongly (higher Bloom's levels tend to be harder) but are not the same axis — a Beginner-difficulty question can technically ask for "Understand" (e.g., "why does Data Governance exist" is conceptual but still low-difficulty if the answer is stated plainly in the source text), and a technically "Apply"-level question can still be Intermediate difficulty if the application is simple and well-signposted. Keeping them as two independent metadata fields (`metadata_schema.md`) lets a future Adaptive Questions engine (`roadmap.md`, Phase 3) tune on either axis independently — e.g., deliberately serving a harder Bloom's level at an easier surface difficulty to build confidence before increasing both together.

## Level-Selection Guidance for Authors

When drafting a question (`authoring_guidelines.md`, Step 4), choose difficulty and Bloom's level together by asking: *"Could a learner answer this from a single memorized fact (Beginner), from correctly classifying an example (Intermediate), from reasoning about a described situation (Advanced), or only by synthesizing multiple Knowledge Areas (Expert)?"* If the honest answer doesn't match the intended level, the stem needs rework, not just a metadata relabel.
