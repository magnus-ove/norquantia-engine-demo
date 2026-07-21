import sys
from norquantia_demo.analyze import analyze_invoice

USAGE = (
    "Usage: norquantia-demo analyze invoice.json"
)


def main():
    if len(sys.argv) < 3:
        print(USAGE)
        return

    command = sys.argv[1]

    if command == "analyze":
        result = analyze_invoice(sys.argv[2])
        print(result)
    else:
        print(USAGE)
