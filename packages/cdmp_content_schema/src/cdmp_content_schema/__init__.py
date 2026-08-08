"""Pydantic v2 schema for CDMP Mastery content records.

One model per content entity in DOMAIN_MODEL.md's "Content Entities"
section, field-for-field matching question_bank/metadata_schema.md's Field
Reference table. This is the one schema shared by validation, the quiz
engine, and (in a later sprint) any API surface -- see TECH_STACK.md's
"Content Schema: Pydantic v2" section for the rationale.
"""

from __future__ import annotations

from cdmp_content_schema.enums import (
    ApprovalStatus,
    BloomsLevel,
    Difficulty,
    KnowledgeAreaCode,
    QuestionType,
    ReviewStatus,
    SourceConfidence,
)
from cdmp_content_schema.knowledge_area import KNOWLEDGE_AREAS, KnowledgeArea, resolve_ka_code
from cdmp_content_schema.question import Question, WhyIncorrect

__all__ = [
    "ApprovalStatus",
    "BloomsLevel",
    "Difficulty",
    "KnowledgeAreaCode",
    "QuestionType",
    "ReviewStatus",
    "SourceConfidence",
    "KnowledgeArea",
    "KNOWLEDGE_AREAS",
    "resolve_ka_code",
    "Question",
    "WhyIncorrect",
]
