"""Result types produced by evaluation and scoring.

See quiz_engine/scoring_engine.md for the design these mirror. v0.1
implements Raw Score, Percentage, and Knowledge Area Score only --
Difficulty Adjustment and the Readiness Indicator depend on session
history this version does not yet persist (quiz_engine/roadmap.md, Phase B).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Union


@dataclass
class AnswerResult:
    """The outcome of grading one submitted answer against one question."""

    question_id: str
    version: str
    knowledge_area: str
    correct: bool
    submitted_answer: Union[str, List[str]]
    correct_answer: Union[str, List[str]]
    incorrect_reasons: List[str] = field(default_factory=list)


@dataclass
class KAScore:
    """Per-Knowledge-Area performance within one session."""

    knowledge_area: str
    correct: int
    total: int

    @property
    def percentage(self) -> float:
        return round((self.correct / self.total) * 100, 1) if self.total else 0.0


@dataclass
class ScoreReport:
    """A completed session's aggregate score, per quiz_engine/scoring_engine.md."""

    total_questions: int
    correct_answers: int
    percentage: float
    ka_breakdown: Dict[str, KAScore]
