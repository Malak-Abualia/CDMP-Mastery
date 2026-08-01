# Quiz Engine — Quiz Modes

## Purpose

Full specification of the five required quiz modes. Each mode is defined as a combination of: a **selection strategy** (`question_selection.md`), a **timing policy**, and a **feedback timing policy** (`feedback_system.md`) — not five independently designed features. This keeps the modes consistent and makes future modes (e.g., `question_bank/roadmap.md`'s Adaptive Questions) addable as new combinations rather than new subsystems.

## Mode Comparison

| Mode | Selection strategy | Timing | Feedback timing | Primary use case (per `roadmap/four_month_plan.md`) |
|---|---|---|---|---|
| Practice | Entire eligible pool, no filter | Unlimited | Immediate, after each question | Daily study, first exposure to new material |
| Knowledge Area | Filtered to one chosen KA | Unlimited (default) | Immediate | Focused study on the week's KA (e.g., Week 3 = Data Governance) |
| Difficulty | Filtered to one chosen tier | Unlimited (default) | Immediate | Calibrating readiness within a tier before advancing |
| Exam Simulation | Full pool, exam-weight-proportional sampling | Timed, matching real exam pacing | Deferred to session end | Full-length practice exams (roadmap Weeks 13–16) |
| Weakness | Driven by Progress Tracking's weak-topic signal | Unlimited (default) | Immediate | Targeted remediation after a scored session reveals gaps |

---

## 1. Practice Mode

- **Selection:** No Knowledge Area or difficulty filter — draws from the entire eligible (Published) pool via `question_selection.md`'s base algorithm.
- **Timing:** Unlimited, as specified. No countdown, no time pressure.
- **Feedback:** Immediate, after every question — full `feedback_system.md` payload (correct/incorrect, explanation, related concept, related flashcards, recommended revision) shown before advancing.
- **Scoring:** All five score types (`scoring_engine.md`) computed and shown, but framed as low-stakes — this is the mode where a learner is expected to get things wrong while still learning, per `CLAUDE.md`'s stated mentoring approach.
- **Session length:** Learner-configurable (e.g., "10 questions" or "until I stop"), not fixed.

## 2. Knowledge Area Mode

- **Selection:** Filtered to exactly one learner-chosen `knowledge_area` (`question_selection.md`'s filter table). No fallback to other KAs if the pool is small — the mode's whole purpose is focus, so silently widening would defeat it; instead, the engine reports the available pool size up front (e.g., "18 questions available in Data Governance") so the learner isn't surprised by a short session.
- **Timing:** Unlimited by default, same as Practice Mode — Knowledge Area Mode is a selection filter layered on Practice Mode's behavior, not a distinct timing/feedback experience.
- **Feedback:** Immediate, same as Practice Mode.
- **Scoring:** The Knowledge Area Score (`scoring_engine.md` §3) is naturally the headline metric here, since the whole session is one KA.
- **Relationship to `roadmap/four_month_plan.md`:** this is the mode a learner uses during a given week's focused study (e.g., Week 5 = Data Quality) — the KA selector should default to whatever Knowledge Area the roadmap indicates is current, if that integration is available, rather than requiring the learner to remember and pick it manually.

## 3. Difficulty Mode

- **Selection:** Filtered to exactly one `difficulty` tier (Beginner/Intermediate/Advanced — Expert reserved, unused per current content). Same no-fallback reasoning as Knowledge Area Mode.
- **Timing:** Unlimited by default.
- **Feedback:** Immediate.
- **Scoring:** The Difficulty Adjustment (`scoring_engine.md` §4) is less relevant here (the session is already one tier), so the plain Percentage is the headline metric instead — used to calibrate "am I ready to move up a tier."
- **Composability note:** Knowledge Area and Difficulty filters are architecturally composable (`question_selection.md`'s selection algorithm supports combining filters), even though they are presented here as two separate top-level modes per this design's explicit five-mode requirement. A future interface may expose "Data Governance, Advanced only" as a combined option without requiring a sixth top-level mode — this is a natural extension, not a new stage.

## 4. Exam Simulation Mode

- **Selection:** Exam-weight-proportional sampling across all Knowledge Areas (`question_selection.md`'s dedicated section on this) — the mode this design most needs to get right, since it's the one making an implicit claim ("this simulates the real exam") that must be honored honestly.
- **Timing:** Timed, matching the real exam's documented pacing (`research/cdmp_exam_overview.md`: 100 questions / 90 minutes, ≈54 seconds/question average; ESL accommodation of +20 minutes is a real exam feature this mode should also offer as an option, not silently omit). A visible countdown is expected; the session auto-submits remaining unanswered questions as incorrect/unattempted when time expires, mirroring real exam conditions.
- **Feedback:** Deferred — no explanations, no correct/incorrect indication, during the session itself, exactly as specified ("no immediate explanations"). Full feedback is delivered only in the end-of-session report, matching the real exam's own closed-book, no-mid-exam-feedback format.
- **Scoring:** All five score types computed at session end; the Readiness Indicator (`scoring_engine.md` §5) is the headline output of this mode specifically, since "would I pass today" is the whole point of running a simulation.
- **Honest coverage disclosure (required, not optional):** Given only 6 of 14 Knowledge Areas currently have content, this mode must not silently run a "100-question exam" that is actually 100 questions drawn unevenly from 6 KAs. Two compliant behaviors, and the engine must pick one explicitly rather than fudge it:
  1. **Partial Mock Exam** — a shorter, clearly-labeled simulation (e.g., "Partial Mock Exam — 6 of 14 Knowledge Areas, ~43 questions at proportional weight") that is honest about its reduced scope, or
  2. **Full-length but explicitly flagged** — a 100-question exam that fills the uncovered Knowledge Areas' weight allocation with a clearly-marked "no content yet" gap in the score breakdown, rather than silently redistributing that weight onto the covered KAs (which would inflate their apparent importance and distort the Readiness Indicator).
  Option 1 is the recommended default until `question_bank/roadmap.md`'s Phase 1 content grows; this is a product decision to confirm at build time, but the *dishonest* third option — quietly treating 6 KAs as if they were the whole exam — is ruled out by this design regardless of which of the two compliant behaviors is chosen.

## 5. Weakness Mode

- **Selection:** Driven entirely by `question_selection.md`'s Weakness Mode algorithm and `progress_integration.md`'s weak-area detection — this mode has no meaning without prior session history (see Cold Start below).
- **Timing:** Unlimited by default, same as Practice Mode.
- **Feedback:** Immediate — the point of this mode is remediation, so immediate explanation matters more here than in any other mode.
- **Scoring:** Tracked the same as other modes, but its most important output is *not* a score — it's whether the previously-weak topic's miss rate improves in the next Weakness or Practice session touching that topic (`progress_integration.md`'s trend tracking is what actually validates whether this mode worked).
- **Cold start handling:** If the learner has no session history yet, this mode cannot select anything meaningfully — per `question_selection.md`, it must say so explicitly and offer an alternative (e.g., "Run a short Practice session first so I can learn where your gaps are") rather than silently degrading into an unlabeled random selection.

---

## Cross-Mode Rules

- **Session persistence applies to every mode** (`progress_integration.md`) — even a Practice Mode session's results feed the weak-area signal Weakness Mode later depends on. No mode is "throwaway" from Progress Tracking's perspective, though a future interface may let a learner explicitly opt a given session out of persistence (e.g., a pure exploration session) — that is an interface-level choice, not a mode-level default.
- **Development-mode content warning** (`data_loading.md`) applies identically across all five modes — if the Loader is running in development mode (serving unreviewed Draft content), every mode's output must carry that warning, not just some.
- **No mode reorders or hides a question's real metadata** — difficulty, Bloom's level, and Knowledge Area shown in feedback/summaries always reflect the question's actual `question_bank/` metadata, never a mode-specific relabeling.
