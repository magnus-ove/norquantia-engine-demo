import json


def analyze_invoice(path):
    with open(path) as f:
        invoice = json.load(f)

    expected_total = (
        invoice["subtotal"] +
        invoice["tax"]
    )

    if expected_total == invoice["total"]:
        return {
            "status": "PASS",
            "message": "Invoice arithmetic is valid."
        }

    return {
        "status": "FAIL",
        "message": "Invoice total mismatch."
    }
