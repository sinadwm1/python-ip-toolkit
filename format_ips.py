"""Format validated addresses from a local text file."""

import argparse
from pathlib import Path

from iptools import format_ips


def main() -> None:
    parser = argparse.ArgumentParser(description="Format an IP address list")
    parser.add_argument("input", type=Path, help="One IP address per line")
    parser.add_argument("--template", default="{ip}", help="Text containing {ip}")
    args = parser.parse_args()
    for line in format_ips(args.input.read_text(encoding="utf-8").splitlines(), args.template):
        print(line)


if __name__ == "__main__":
    main()
