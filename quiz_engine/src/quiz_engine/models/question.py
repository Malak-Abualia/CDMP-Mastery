"""The Question model: the in-memory representation of one question_bank record.

Field set mirrors question_bank/metadata_schema.md's Field Reference table.
Construction from a raw dict happens in loader/yaml_loader.py, not here --
this module only defines the shape, it does not parse or validate.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class WhyIncorrect:
    """One entry from a question's `why_incorrect` list."""

    option: str
    reason: str


@dataclass
class Question:
    """One question record, as defined by question_bank/metadata_schema.md."""

    question_id: str
    version: str
    knowledge_area: str
    topic: str
    subtopic: str
    difficulty: str
    blooms_level: str
    learning_objective: str
    dama_concept: Optional[str]
    industry_practice_concept: Optional[str]
    keywords: List[str]
    estimated_solving_time: int
    question_type: str
    stem: str
    answer_choices: List[str]
    correct_answer: Union[str, List[str]]
    explanation: str
    why_incorrect: List[WhyIncorrect]
    related_knowledge_areas: List[str]
    related_flashcards: List[str]
    related_exercises: List[str]
    references: List[str]
    source_confidence: str
    review_status: str
    approval_status: str
    author: str
    reviewer: List[str]
    creation_date: str
    last_modified: str
    source_path: str = field(default="")

    @property
    def is_multi_select(self) -> bool:
        """True if `correct_answer` is a set of options rather than a single one.

        Per quiz_engine/answer_evaluation.md's "Core Rule: Evaluate by
        Shape, Not by Label" -- some Scenario-Based questions carry a
        multi-select-shaped answer (see GOV-016, documented in
        research/question_bank_audit.md), so this must never be inferred
        from `question_type` alone.
        """
        return isinstance(self.correct_answer, list)
