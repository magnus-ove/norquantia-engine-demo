# Norquantia Engine Demo

Public demonstration of deterministic invoice validation for ERP and finance systems.

![Release](https://img.shields.io/github/v/release/magnus-ove/norquantia-engine-demo)
![CI](https://github.com/magnus-ove/norquantia-engine-demo/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)
![Status](https://img.shields.io/badge/status-active-success)

---

## Features

- Deterministic invoice arithmetic validation
- Document sign consistency checks
- JSON diagnostics output
- Synthetic invoice examples
- Automated testing

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

## Example

```bash
norquantia-demo analyze examples/invoice_valid.json
```

Expected output:

```json
{
  "status": "PASS",
  "rules_evaluated": 2,
  "passed": 2,
  "failed": 0
}
```

---

This repository intentionally excludes:

- Country-specific tax logic
- Proprietary mappings
- Customer integrations
- AI reasoning
- Proprietary Norquantia technologies

## Example usage

```bash
norquantia-demo analyze examples/invoice_valid.json
```

Expected result:

```json
{
  "status": "PASS"
}
```

## Roadmap

- [x] Package structure
- [x] CLI entrypoint
- [ ] Invoice analysis command
- [ ] JSON diagnostics
- [ ] Automated tests
- [ ] CI pipeline
