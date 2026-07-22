<div align="center">

# Norquantia Engine Demo

### Deterministic Invoice Validation

**ERP • Finance • Tax • Structured JSON**

Public demonstration of deterministic invoice validation for ERP and finance systems.

![Release](https://img.shields.io/github/v/release/magnus-ove/norquantia-engine-demo)
![CI](https://github.com/magnus-ove/norquantia-engine-demo/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)
![Status](https://img.shields.io/badge/status-active-success)

</div>

---

## Public Demonstration Notice

This repository is a public demonstration of deterministic validation concepts.
It contains only synthetic examples and public demo logic. It does not contain
the proprietary Norquantia Core Engine, production rule sets, benchmark datasets,
customer data or customer integrations, or commercial production implementations.

The production Norquantia Core Engine remains private and is maintained separately
from this public demonstration repository.

---

## Features

- Deterministic invoice arithmetic validation
- Synthetic document-type and invoice-number checks
- Stable JSON diagnostics, summary, and metadata output
- Synthetic invoice examples
- Automated testing
- GitHub Actions CI

---

## Architecture

```text
Invoice JSON
      ↓
Validation Rules
      ↓
Diagnostics
      ↓
JSON Result
```

---

## Installation

Norquantia Engine Demo requires Python 3.12 or newer. Install the project and
development tools from the repository root:

```bash
python -m pip install ".[dev]"
```

---

## Example Usage

The valid example exits with status `0`:

```bash
norquantia-demo analyze examples/invoice_valid.json
```

The invalid example exits with status `1`:

```bash
norquantia-demo analyze examples/invoice_invalid.json
```

```json
{
  "documentType": "invoice",
  "validationStatus": "invalid",
  "summary": {
    "errors": 1,
    "warnings": 0,
    "checksPerformed": 3
  },
  "diagnostics": [
    {
      "code": "DEMO_TOTAL_MISMATCH",
      "severity": "error",
      "field": "total",
      "message": "Synthetic subtotal plus tax does not match total.",
      "expected": "1250",
      "actual": "1400"
    }
  ],
  "metadata": {
    "engine": "Norquantia Engine Demo",
    "engineVersion": "0.2.0",
    "deterministic": true
  }
}
```

All checks and examples in this repository are intentionally synthetic and are
independent of the private Norquantia Core Engine.

---

## Scope

This public repository intentionally excludes:

- Country-specific tax logic
- Proprietary mappings
- Customer integrations
- AI reasoning
- Commercial Norquantia IP

---

## Vision

Norquantia Engine Demo showcases selected public capabilities related to deterministic validation for ERP and finance systems.

Commercial Norquantia technology, proprietary tax engines, customer integrations and AI workflows are intentionally excluded from this repository.

---

## Releases and Roadmap

### v0.1.0
- Initial public demonstration release
- Arithmetic validation
- Structured validation diagnostics
- Python package structure
- CLI interface
- Automated testing
- GitHub Actions CI

### v0.2.0
- Deterministic invoice validation
- Stable structured JSON diagnostics
- CLI verification examples and automated checks
- Clear separation from proprietary Norquantia technology

### Future
- HTML reporting
- ERP integrations
- Norquantia Flow compatibility

---

## License

This public demonstration repository is available under the [MIT License](LICENSE).
