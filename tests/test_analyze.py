from norquantia_demo.analyze import analyze_invoice


def test_valid_invoice():
    result = analyze_invoice(
        "examples/invoice_valid.json"
    )

    assert result["status"] == "PASS"


def test_invalid_invoice():
    result = analyze_invoice(
        "examples/invoice_invalid.json"
    )

    assert result["status"] == "FAIL"
