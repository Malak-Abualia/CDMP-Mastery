"""Enum-constrained fields from question_bank/metadata_schema.md's Field Reference table.

Every value here mirrors an authoritative source document rather than an
assumption:
- Difficulty: question_bank/difficulty_framework.md
- BloomsLevel: question_bank/difficulty_framework.md ([Industry Practice] --
  Bloom's Taxonomy is a general pedagogical framework, not DAMA-specific)
- QuestionType: question_bank/authoring_guidelines.md
- SourceConfidence: research/source_map.md's priority tiers
- ReviewStatus: question_bank/question_lifecycle.md's state machine
- ApprovalStatus: question_bank/question_lifecycle.md, "Approval"
- KnowledgeAreaCode: question_bank/naming_conventions.md's code table
"""

from __future__ import annotations

from enum import Enum


class Difficulty(str, Enum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"
    EXPERT = "Expert"


class BloomsLevel(str, Enum):
    REMEMBER = "Remember"
    UNDERSTAND = "Understand"
    APPLY = "Apply"
    ANALYZE = "Analyze"
    EVALUATE = "Evaluate"
    CREATE = "Create"


class QuestionType(str, Enum):
    MULTIPLE_CHOICE = "Multiple Choice"
    MULTIPLE_SELECT = "Multiple Select"
    TRUE_FALSE = "True/False"
    SCENARIO_BASED = "Scenario-Based"
    MATCHING = "Matching"
    ORDERING = "Ordering"
    MINI_CASE_STUDY = "Mini Case Study"


class SourceConfidence(str, Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class ReviewStatus(str, Enum):
    DRAFT = "Draft"
    TECHNICAL_REVIEW = "TechnicalReview"
    DAMA_REVIEW = "DAMAReview"
    APPROVAL = "Approval"
    PUBLISHED = "Published"
    RETIRED = "Retired"


class ApprovalStatus(str, Enum):
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class KnowledgeAreaCode(str, Enum):
    GOV = "GOV"
    ARCH = "ARCH"
    MODEL = "MODEL"
    STOR = "STOR"
    SEC = "SEC"
    INTEG = "INTEG"
    DOC = "DOC"
    MASTER = "MASTER"
    DWBI = "DWBI"
    META = "META"
    QUAL = "QUAL"
    BIGDATA = "BIGDATA"
    MAT = "MAT"
    ETH = "ETH"
