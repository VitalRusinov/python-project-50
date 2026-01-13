#!/usr/bin/env python3
"""CLI entry point for gendiff."""

import sys

from gendiff import generate_diff
from gendiff.cli import parse_args


def main():
    try:
        args = parse_args()
        diff = generate_diff(args.first_file, args.second_file, args.format)
        print(diff)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
