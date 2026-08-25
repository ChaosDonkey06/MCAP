from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="mcap",
        description="MCAP command-line interface",
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="Show package version and exit",
    )
    args = parser.parse_args()

    if args.version:
        from mcap import __version__
        print(__version__)
        return

    parser.print_help()


if __name__ == "__main__":
    main()
