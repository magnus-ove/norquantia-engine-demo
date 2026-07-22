import json
from pathlib import Path

from norquantia_demo import __version__
from norquantia_demo.analyze import (
    analyze_invoice,
    load_invoice,
    validate_invoice,
)
from norquantia_demo.cli import main

FIXTURES = Path(__file__).parent / "fixtures"


def test_valid_invoice_has_complete_stable_output_shape() -> None:
    result = analyze_invoice("examples/invoice_valid.json")

    assert result == {
        "documentType": "invoice",
        "validationStatus": "valid",
        "summary": {
            "errors": 0,
            "warnings": 0,
            "checksPerformed": 3,
        },
        "diagnostics": [],
        "metadata": {
            "engine": "Norquantia Engine Demo",
            "engineVersion": __version__,
            "deterministic": True,
        },
    }


def test_invalid_invoice_has_stable_diagnostic_and_summary() -> None:
    result = analyze_invoice("examples/invoice_invalid.json")

    assert result["validationStatus"] == "invalid"
    assert result["summary"] == {
        "errors": 1,
        "warnings": 0,
        "checksPerformed": 3,
    }
    assert result["diagnostics"] == [
        {
            "code": "DEMO_TOTAL_MISMATCH",
            "severity": "error",
            "field": "total",
            "message": (
                "Synthetic subtotal plus tax does not match total."
            ),
            "expected": "1250",
            "actual": "1400",
        }
    ]


def test_diagnostic_order_is_fixed_and_deterministic() -> None:
    payload = load_invoice(FIXTURES / "invoice_multiple_diagnostics.json")

    first = validate_invoice(payload)
    second = validate_invoice(payload)

    assert [item.code for item in first.diagnostics] == [
        "DEMO_DOCUMENT_TYPE_UNSUPPORTED",
        "DEMO_INVOICE_NUMBER_RECOMMENDED",
        "DEMO_TOTAL_MISMATCH",
    ]
    assert first.summary.errors == 2
    assert first.summary.warnings == 1
    assert first == second
    assert first.to_json() == second.to_json()


def test_result_serializes_as_valid_json() -> None:
    result = validate_invoice(
        {
            "documentType": "invoice",
            "invoice_number": "INV-JSON-001",
            "subtotal": 100,
            "tax": 25,
            "total": 125,
        }
    )

    serialized = result.to_json()

    assert json.loads(serialized) == result.to_dict()


def test_cli_prints_json_and_returns_invalid_status(capsys) -> None:
    exit_code = main(["analyze", "examples/invoice_invalid.json"])

    captured = capsys.readouterr()
    output = json.loads(captured.out)
    assert exit_code == 1
    assert captured.err == ""
    assert output["validationStatus"] == "invalid"
    assert output["diagnostics"][0]["code"] == "DEMO_TOTAL_MISMATCH"
