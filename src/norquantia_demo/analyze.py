"""Intentionally synthetic validation for the public demo repository."""

from __future__ import annotations

import json
from decimal import Decimal, InvalidOperation
from pathlib import Path

from . import __version__
from .models import (
    Diagnostic,
    Metadata,
    Severity,
    Summary,
    ValidationResult,
    ValidationStatus,
)

DEMO_ENGINE = "Norquantia Engine Demo"
SUPPORTED_DOCUMENT_TYPE = "invoice"
CHECKS_PERFORMED = 3
_MISSING = object()


class DemoInputError(ValueError):
    """Raised when a synthetic demo input cannot be loaded."""


def _display_actual(value: object) -> object:
    return "<missing>" if value is _MISSING else value


def _decimal(value: object) -> Decimal | None:
    if isinstance(value, bool) or not isinstance(value, (int, float, str)):
        return None
    try:
        return Decimal(str(value))
    except InvalidOperation:
        return None


def _decimal_text(value: Decimal) -> str:
    return format(value, "f")


def validate_invoice(invoice: dict[str, object]) -> ValidationResult:
    """Run three fixed checks created only for this public synthetic demo."""
    diagnostics: list[Diagnostic] = []

    document_type = invoice.get("documentType", _MISSING)
    if document_type != SUPPORTED_DOCUMENT_TYPE:
        diagnostics.append(
            Diagnostic(
                code="DEMO_DOCUMENT_TYPE_UNSUPPORTED",
                severity=Severity.ERROR,
                field="documentType",
                message="The synthetic demo document type is not supported.",
                expected=SUPPORTED_DOCUMENT_TYPE,
                actual=_display_actual(document_type),
            )
        )

    invoice_number = invoice.get("invoice_number", _MISSING)
    if not isinstance(invoice_number, str) or invoice_number.strip() == "":
        diagnostics.append(
            Diagnostic(
                code="DEMO_INVOICE_NUMBER_RECOMMENDED",
                severity=Severity.WARNING,
                field="invoice_number",
                message="A synthetic demo invoice number is recommended.",
                expected="non-empty string",
                actual=_display_actual(invoice_number),
            )
        )

    amount_fields = ("subtotal", "tax", "total")
    decimal_amounts = {
        field: _decimal(invoice.get(field, _MISSING))
        for field in amount_fields
    }
    invalid_fields = [
        field for field in amount_fields if decimal_amounts[field] is None
    ]
    if invalid_fields:
        diagnostics.append(
            Diagnostic(
                code="DEMO_AMOUNTS_INVALID",
                severity=Severity.ERROR,
                field="subtotal,tax,total",
                message="Synthetic demo amounts must be numeric.",
                expected="numeric values",
                actual=invalid_fields,
            )
        )
    else:
        subtotal = decimal_amounts["subtotal"]
        tax = decimal_amounts["tax"]
        total = decimal_amounts["total"]
        assert subtotal is not None and tax is not None and total is not None
        calculated_total = subtotal + tax
        if calculated_total != total:
            diagnostics.append(
                Diagnostic(
                    code="DEMO_TOTAL_MISMATCH",
                    severity=Severity.ERROR,
                    field="total",
                    message="Synthetic subtotal plus tax does not match total.",
                    expected=_decimal_text(calculated_total),
                    actual=_decimal_text(total),
                )
            )

    errors = sum(item.severity is Severity.ERROR for item in diagnostics)
    warnings = sum(item.severity is Severity.WARNING for item in diagnostics)
    output_document_type = (
        document_type if isinstance(document_type, str) else "unknown"
    )
    return ValidationResult(
        document_type=output_document_type,
        validation_status=(
            ValidationStatus.INVALID if errors else ValidationStatus.VALID
        ),
        summary=Summary(
            errors=errors,
            warnings=warnings,
            checks_performed=CHECKS_PERFORMED,
        ),
        diagnostics=tuple(diagnostics),
        metadata=Metadata(
            engine=DEMO_ENGINE,
            engine_version=__version__,
            deterministic=True,
        ),
    )


def load_invoice(path: str | Path) -> dict[str, object]:
    """Load a synthetic demo invoice as a JSON object."""
    try:
        source = Path(path).read_text(encoding="utf-8")
    except OSError as error:
        raise DemoInputError(f"Could not read demo input: {error}") from error
    try:
        invoice = json.loads(source)
    except json.JSONDecodeError as error:
        raise DemoInputError(f"Demo input is not valid JSON: {error}") from error
    if not isinstance(invoice, dict):
        raise DemoInputError("Demo input must be a JSON object")
    return invoice


def analyze_invoice(path: str | Path) -> dict[str, object]:
    """Load and validate one synthetic demo invoice."""
    return validate_invoice(load_invoice(path)).to_dict()
