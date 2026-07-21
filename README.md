<div align="center">

# Norquantia Engine Demo

### Deterministic Invoice Validation

**ERP • Finance • Tax • AI Ready**

Public demonstration of deterministic invoice validation for ERP and finance systems.

![Release](https://img.shields.io/github/v/release/magnus-ove/norquantia-engine-demo)
![CI](https://github.com/magnus-ove/norquantia-engine-demo/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)
![Status](https://img.shields.io/badge/status-active-success)

</div>

---

## Features

- Deterministic invoice arithmetic validation
- Document sign consistency checks
- JSON diagnostics output
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

## Example Usage

```bash
norquantia-demo analyze examples/invoice_valid.json
```

Expected output:

```json
{
  "status": "PASS"
}
```

Invalid invoice example:

```json
{
  "status": "FAIL",
  "message": "Invoice total mismatch."
}
```

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

## Roadmap

### v0.1.0
- Initial public demonstration release
- Arithmetic validation
- PASS / FAIL diagnostics
- Python package structure
- CLI interface
- Automated testing
- GitHub Actions CI

### v0.2.0
- Enhanced diagnostics
- Batch invoice processing
- Improved JSON output
- Additional validation rules

### Future
- HTML reporting
- ERP integrations
- Norquantia Flow compatibility
