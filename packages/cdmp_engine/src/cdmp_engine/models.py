"""Runtime domain models: Quiz, QuizSession, Answer, QuizResult.

Per quiz_engine/architecture.md's "Stateless core, stateful session"
principle: `Quiz` (the assembled, ordered question set) and `Answer`/
`QuizResult` (evaluation/scoring output) are immutable value objects: pure
data produced by a pure function of their inputs. `QuizSession` is the one
mutable, stateful object in this package -- it tracks how far through the
Quiz the learner has progressed and the Answers recorded so far, held in
memory for the CLI process's lifetime (no persistence in this sprint; see
DOMAIN_MODEL.md's QuizSession/Attempt for the future durable shape this
mirrors conceptually).
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field

from cdmp_content_schema import Difficulty, KnowledgeAreaCode, Question


class QuizMode(str, Enum):
    """The three modes this sprint's Selection Engine supports.

    Exam Simulation and Weakness Mode both require durable cross-session
    history (exam-weight sampling against persisted content stats; a
    weak-area signal computed from prior sessions) that does not exist
    without the persistence layer explicitly out of scope for this sprint
    (quiz_engine/quiz_modes.md) -- so they are not modeled here.
    """

    PRACTICE = "practice"
    KNOWLEDGE_AREA = "knowledge_area"
    DIFFICULTY = "difficulty"


class Quiz(BaseModel):
    """The assembled, ordered question set for one session -- Selection's output."""

    model_config = ConfigDict(frozen=True)

    mode: QuizMode
    knowledge_area: KnowledgeAreaCode | None = None
    difficulty: Difficulty | None = None
    questions: tuple[Question, ...] = Field(min_length=1)
    dev_unreviewed: bool = False


class Answer(BaseModel):
    """One learner response to one question -- Evaluation's output for that question.

    Classification fields (`knowledge_area`, `topic`, `difficulty`) are
    copied from the Question at answer time rather than looked up live,
    mirroring DOMAIN_MODEL.md's Attempt entity: "so historical analysis
    remains accurate even if the question's classification changes."
    """

    model_config = ConfigDict(frozen=True)

    question_id: str
    question_version: str
    knowledge_area: KnowledgeAreaCode
    topic: str
    difficulty: Difficulty
    selected: list[str] | None
    """Selected option labels, in the order submitted. `None` means skipped --
    distinct from an empty selection, which is not a valid submission."""
    correct: bool | None
    """`None` means skipped: excluded from scoring denominators, never
    counted as incorrect (cli_design.md's explicit-skip requirement)."""
    missed_correct: list[str] = Field(default_factory=list)
    wrongly_included: list[str] = Field(default_factory=list)
    why_incorrect_messages: list[str] = Field(default_factory=list)
    time_taken_seconds: float | None = None

    @property
    def skipped(self) -> bool:
        return self.selected is None


class QuizSession(BaseModel):
    """The one mutable, stateful object in this package."""

    quiz: Quiz
    answers: list[Answer] = Field(default_factory=list)
    started_at: datetime = Field(default_factory=datetime.now)
    completed_at: datetime | None = None

    @property
    def current_index(self) -> int:
        return len(self.answers)

    @property
    def is_complete(self) -> bool:
        return self.current_index >= len(self.quiz.questions)

    @property
    def total_questions(self) -> int:
        return len(self.quiz.questions)

    def current_question(self) -> Question:
        if self.is_complete:
            raise IndexError("QuizSession has no more questions -- session is already complete")
        return self.quiz.questions[self.current_index]

    def record_answer(self, answer: Answer) -> None:
        if self.is_complete:
            raise IndexError("Cannot record an answer -- session is already complete")
        expected = self.current_question()
        if answer.question_id != expected.question_id or answer.question_version != expected.version:
            raise ValueError(
                f"Answer is for {answer.question_id} v{answer.question_version}, "
                f"but the current question is {expected.question_id} v{expected.version}"
            )
        self.answers.append(answer)
        if self.is_complete:
            self.completed_at = datetime.now()


class ScoreBreakdownEntry(BaseModel):
    """One row of a Knowledge-Area or Topic score breakdown (scoring_engine.md §3)."""

    model_config = ConfigDict(frozen=True)

    label: str
    correct: int
    total: int
    percentage: float
    low_confidence: bool
    """True when `total` is below the configured minimum sample size --
    a score from 1-2 questions swings too easily to be presented with the
    same weight as a well-sampled one (scoring_engine.md §3)."""


class WeakArea(BaseModel):
    """A topic or Knowledge Area flagged weak within this single session.

    Scoped to the current session's own attempts -- not the persisted,
    cross-session `WeakArea` entity DOMAIN_MODEL.md defines for the
    (out-of-scope-this-sprint) runtime schema, which Weakness Mode would
    read from in a later sprint.
    """

    model_config = ConfigDict(frozen=True)

    label: str
    scope: str
    """Either "topic" or "knowledge_area"."""
    miss_rate: float
    sample_size: int


class QuizResult(BaseModel):
    """The end-of-session score record (scoring_engine.md's "Score Record Shape")."""

    model_config = ConfigDict(frozen=True)

    raw_score: int
    questions_attempted: int
    questions_skipped: int
    percentage: float
    knowledge_area_breakdown: tuple[ScoreBreakdownEntry, ...]
    topic_breakdown: tuple[ScoreBreakdownEntry, ...]
    weak_areas: tuple[WeakArea, ...]
