"""Shared pytest fixtures for cdmp_engine's Question Loader tests."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

import pytest
import yaml


def make_question_dict(**overrides: Any) -> Dict[str, Any]:
    """A minimal, schema-valid question dict (per metadata_schema.md), with overrides."""
    base: Dict[str, Any] = {
        "question_id": "TEST-001",
        "version": "1.0",
        "knowledge_area": "GOV",
        "topic": "Roles and Accountability",
        "subtopic": "Data Owner",
        "difficulty": "Beginner",
        "blooms_level": "Remember",
        "learning_objective": "Recall the Data Owner role.",
        "dama_concept": "Data Owner",
        "industry_practice_concept": None,
        "keywords": ["data owner"],
        "estimated_solving_time": 25,
        "question_type": "Multiple Choice",
        "stem": "Which role is accountable for a data domain?",
        "answer_choices": ["A) Custodian", "B) Owner", "C) Engineer", "D) Architect"],
        "correct_answer": "B",
        "explanation": "The Data Owner is accountable.",
        "why_incorrect": [
            {"option": "A", "reason": "Custodian implements, does not own."},
            {"option": "C", "reason": "Engineer is usually the Custodian."},
            {"option": "D", "reason": "Architect designs structures, not domain ownership."},
        ],
        "related_knowledge_areas": ["GOV"],
        "related_flashcards": ["Data Owner"],
        "related_exercises": [],
        "references": ["knowledge_base/data_governance.md, Section 3"],
        "source_confidence": "High",
        "review_status": "Published",
        "approval_status": "Approved",
        "author": "test-author",
        "reviewer": ["test-reviewer"],
        "creation_date": "2026-08-01",
        "last_modified": "2026-08-01",
    }
    base.update(overrides)
    return base


@pytest.fixture
def question_dict_factory():
    return make_question_dict


@pytest.fixture
def questions_root(tmp_path: Path) -> Path:
    return tmp_path / "questions"


@pytest.fixture
def write_question(questions_root: Path):
    def _write(filename: str, ka_folder: str = "data_governance", **overrides: Any) -> Path:
        data = make_question_dict(**overrides)
        target_dir = questions_root / ka_folder
        target_dir.mkdir(parents=True, exist_ok=True)
        path = target_dir / filename
        path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
        return path

    return _write
