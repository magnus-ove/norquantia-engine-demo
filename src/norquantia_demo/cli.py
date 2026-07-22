"""Command-line interface for the public synthetic demo."""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Sequence
from pathlib import Path

from .analyze import DemoInputError, load_invoice, validate_invoice
from .models import ValidationStatus


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="norquantia-demo")
    subparsers = parser.add_subparsers(dest="command", required=True)
    analyze_parser = subparsers.add_parser(
        "analyze",
        help="analyze one synthetic demo invoice",
    )
    analyze_parser.add_argument("invoice", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the synthetic demo CLI."""
    arguments = build_parser().parse_args(argv)
    if arguments.command != "analyze":
        return 2

    try:
        invoice = load_invoice(arguments.invoice)
    except DemoInputError as error:
        print(
            json.dumps(
                {
                    "error": {
                        "code": "DEMO_INPUT_ERROR",
                        "message": str(error),
                    }
                },
                indent=2,
            ),
            file=sys.stderr,
        )
        return 2

    output = validate_invoice(invoice)
    print(output.to_json())
    return 0 if output.validation_status is ValidationStatus.VALID else 1


if __name__ == "__main__":
    raise SystemExit(main())
