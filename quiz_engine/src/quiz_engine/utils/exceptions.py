"""Custom exceptions for the Quiz Engine."""

from __future__ import annotations


class QuizEngineError(Exception):
    """Base class for all Quiz Engine errors."""


class QuestionParseError(QuizEngineError):
    """Raised when a question file cannot be parsed as valid YAML."""

    def __init__(self, path: str, reason: str) -> None:
        self.path = path
        self.reason = reason
        super().__init__(f"{path}: {reason}")


class NoQuestionsAvailableError(QuizEngineError):
    """Raised when a quiz is requested but no questions match the given filters."""
