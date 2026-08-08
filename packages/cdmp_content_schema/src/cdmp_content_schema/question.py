"""The Question model: field-for-field mirror of metadata_schema.md's Field Reference table.

Two validation rules matter more than the rest of this file combined:

1. **Evaluate/validate by shape, not by label** (answer_evaluation.md's Core
   Rule). `correct_answer` is a string for a single-answer question and a
   list of strings for a multiple-select one -- and, critically, that shape
   is *not* implied by `question_type` (GOV-016 is labeled "Scenario-Based"
   but is Multiple-Select-shaped). This model validates the shape it is
   actually given, never branching on the type label.
2. **Primary Knowledge Area consistency** (taxonomy.md, "Cross-Knowledge-Area
   Tagging"): `related_knowledge_areas` must list every KA a question
   touches with the primary one first, so it always agrees with the
   standalone `knowledge_area` field rather than the two silently drifting
   apart.
"""

from __future__ import annotations

import re
from datetime import date

from pydantic import BaseModel, ConfigDict, Field, model_validator

from cdmp_content_schema.enums import (
    ApprovalStatus,
    BloomsLevel,
    Difficulty,
    KnowledgeAreaCode,
    QuestionType,
    ReviewStatus,
    SourceConfidence,
)

_QUESTION_ID_PATTERN = re.compile(r"^[A-Z]+-\d+$")
_VERSION_PATTERN = re.compile(r"^\d+\.\d+$")
_OPTION_LABEL_PATTERN = re.compile(r"^([A-Za-z0-9]+)\)")


def _extract_label(choice: str) -> str | None:
    """Pull the leading label (e.g. "A" from "A) some text") off an answer choice."""
    match = _OPTION_LABEL_PATTERN.match(choice.strip())
    return match.group(1) if match else None


class WhyIncorrect(BaseModel):
    """One entry from a question's `why_incorrect` list."""

    model_config = ConfigDict(frozen=True)

    option: str
    reason: str = Field(min_length=1)


class Question(BaseModel):
    """One question record, as defined by question_bank/metadata_schema.md."""

    model_config = ConfigDict(frozen=True, use_enum_values=False)

    question_id: str = Field(pattern=_QUESTION_ID_PATTERN.pattern)
    version: str = Field(pattern=_VERSION_PATTERN.pattern)
    knowledge_area: KnowledgeAreaCode
    topic: str = Field(min_length=1)
    subtopic: str = Field(min_length=1)
    difficulty: Difficulty
    blooms_level: BloomsLevel
    learning_objective: str = Field(min_length=1)
    dama_concept: str | None = None
    industry_practice_concept: str | None = None
    keywords: list[str] = Field(min_length=1)
    estimated_solving_time: int = Field(gt=0)
    question_type: QuestionType
    stem: str = Field(min_length=1)
    answer_choices: list[str]
    correct_answer: str | list[str] | bool
    explanation: str = Field(min_length=1)
    why_incorrect: list[WhyIncorrect] = Field(default_factory=list)
    related_knowledge_areas: list[KnowledgeAreaCode] = Field(min_length=1)
    related_flashcards: list[str] = Field(default_factory=list)
    related_exercises: list[str] = Field(default_factory=list)
    references: list[str] = Field(min_length=1)
    source_confidence: SourceConfidence
    review_status: ReviewStatus
    approval_status: ApprovalStatus
    author: str = Field(min_length=1)
    reviewer: list[str] = Field(default_factory=list)
    creation_date: date
    last_modified: date
    source_path: str = ""

    @property
    def is_multi_select(self) -> bool:
        """True if `correct_answer` is a set of options rather than a single one.

        Never inferred from `question_type` -- see module docstring.
        """
        return isinstance(self.correct_answer, list)

    @model_validator(mode="after")
    def _check_primary_knowledge_area_is_first(self) -> "Question":
        if not self.related_knowledge_areas or self.related_knowledge_areas[0] != self.knowledge_area:
            raise ValueError(
                "related_knowledge_areas must list the primary knowledge_area "
                f"({self.knowledge_area.value}) first; got {self.related_knowledge_areas!r}"
            )
        return self

    @model_validator(mode="after")
    def _check_reviewer_present_past_draft(self) -> "Question":
        if self.review_status != ReviewStatus.DRAFT and not self.reviewer:
            raise ValueError(
                f"reviewer must be non-empty once review_status is {self.review_status.value!r}"
            )
        return self

    @model_validator(mode="after")
    def _check_last_modified_not_before_creation(self) -> "Question":
        if self.last_modified < self.creation_date:
            raise ValueError(
                f"last_modified ({self.last_modified}) is before creation_date ({self.creation_date})"
            )
        return self

    @model_validator(mode="after")
    def _check_correct_answer_shape(self) -> "Question":
        if isinstance(self.correct_answer, bool):
            if self.question_type != QuestionType.TRUE_FALSE:
                raise ValueError(
                    "a boolean correct_answer is only valid for question_type "
                    f"'True/False', got {self.question_type.value!r}"
                )
            return self

        labels = [_extract_label(choice) for choice in self.answer_choices]
        if any(label is None for label in labels):
            raise ValueError(
                "every answer_choices entry must start with a label, e.g. 'A) ...'"
            )
        valid_labels = set(labels)

        if isinstance(self.correct_answer, str):
            if self.correct_answer not in valid_labels:
                raise ValueError(
                    f"correct_answer {self.correct_answer!r} is not among "
                    f"answer_choices labels {sorted(valid_labels)}"
                )
        else:
            if not self.correct_answer:
                raise ValueError("correct_answer list must not be empty")
            if len(set(self.correct_answer)) != len(self.correct_answer):
                raise ValueError(f"correct_answer contains duplicate labels: {self.correct_answer!r}")
            unknown = [label for label in self.correct_answer if label not in valid_labels]
            if unknown:
                raise ValueError(
                    f"correct_answer labels {unknown} are not among answer_choices labels {sorted(valid_labels)}"
                )
        return self

    @model_validator(mode="after")
    def _check_why_incorrect_options_are_real_distractors(self) -> "Question":
        if isinstance(self.correct_answer, bool):
            return self
        correct_labels = (
            {self.correct_answer} if isinstance(self.correct_answer, str) else set(self.correct_answer)
        )
        valid_labels = {_extract_label(choice) for choice in self.answer_choices}
        for entry in self.why_incorrect:
            if entry.option not in valid_labels:
                raise ValueError(
                    f"why_incorrect option {entry.option!r} is not among answer_choices labels {sorted(valid_labels)}"
                )
            if entry.option in correct_labels:
                raise ValueError(
                    f"why_incorrect option {entry.option!r} is itself a correct answer, not a distractor"
                )
        return self
