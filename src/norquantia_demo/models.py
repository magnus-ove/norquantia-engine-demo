"""Stable public JSON models for the synthetic Norquantia demo."""

from __future__ import annotations

import json
from dataclasses import dataclass
from enum import StrEnum

_UNSET = object()


class Severity(StrEnum):
    """Stable diagnostic severities exposed by the demo."""

    ERROR = "error"
    WARNING = "warning"


class ValidationStatus(StrEnum):
    """Stable validation states exposed by the demo."""

    VALID = "valid"
    INVALID = "invalid"


@dataclass(frozen=True, slots=True)
class Diagnostic:
    """One deterministic synthetic validation diagnostic."""

    code: str
    severity: Severity
    field: str
    message: str
    expected: object = _UNSET
    actual: object = _UNSET

    def to_dict(self) -> dict[str, object]:
        """Return the stable diagnostic structure."""
        output: dict[str, object] = {
            "code": self.code,
            "severity": self.severity.value,
            "field": self.field,
            "message": self.message,
        }
        if self.expected is not _UNSET:
            output["expected"] = self.expected
        if self.actual is not _UNSET:
            output["actual"] = self.actual
        return output


@dataclass(frozen=True, slots=True)
class Summary:
    """Counts produced by the fixed synthetic demo checks."""

    errors: int
    warnings: int
    checks_performed: int

    def to_dict(self) -> dict[str, int]:
        """Return the stable summary structure."""
        return {
            "errors": self.errors,
            "warnings": self.warnings,
            "checksPerformed": self.checks_performed,
        }


@dataclass(frozen=True, slots=True)
class Metadata:
    """Identify the public demo without implying private-engine behavior."""

    engine: str
    engine_version: str
    deterministic: bool

    def to_dict(self) -> dict[str, object]:
        """Return the stable metadata structure."""
        return {
            "engine": self.engine,
            "engineVersion": self.engine_version,
            "deterministic": self.deterministic,
        }


@dataclass(frozen=True, slots=True)
class ValidationResult:
    """Complete stable output contract for the public synthetic demo."""

    document_type: str
    validation_status: ValidationStatus
    summary: Summary
    diagnostics: tuple[Diagnostic, ...]
    metadata: Metadata

    def to_dict(self) -> dict[str, object]:
        """Return the complete stable JSON-compatible structure."""
        return {
            "documentType": self.document_type,
            "validationStatus": self.validation_status.value,
            "summary": self.summary.to_dict(),
            "diagnostics": [item.to_dict() for item in self.diagnostics],
            "metadata": self.metadata.to_dict(),
        }

    def to_json(self) -> str:
        """Serialize deterministically as valid formatted JSON."""
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)
