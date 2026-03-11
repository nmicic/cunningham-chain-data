#!/usr/bin/env python3
# Copyright (c) 2026 Nenad Mićić <nenad@micic.be>
# SPDX-License-Identifier: Apache-2.0
"""
make_snapshot_csv.py — Convert raw CC roots to normalized CSV.

Input format (one root per line):
    CC10 0xHEXVALUE DIGITS

Output CSV columns:
    cc,root_hex,digits,bits

Usage:
    python3 make_snapshot_csv.py input.txt output.csv
    python3 make_snapshot_csv.py input.txt output.csv --limit 1000
"""

import argparse
import csv
import sys


def hex_to_bits(hex_str):
    """Return the bit length of a hex value (with or without 0x prefix)."""
    return int(hex_str, 16).bit_length()


def convert(input_path, output_path, limit=None):
    count = 0
    skipped = 0
    with open(input_path, "r") as fin, open(output_path, "w", newline="") as fout:
        writer = csv.writer(fout)
        writer.writerow(["cc", "root_hex", "digits", "bits"])
        for lineno, line in enumerate(fin, 1):
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) < 3 or not parts[0].startswith("CC"):
                skipped += 1
                print(
                    f"WARNING: skipped malformed line {lineno}: {line!r}",
                    file=sys.stderr,
                )
                continue
            cc_label = parts[0]       # e.g. "CC10"
            root_hex = parts[1]       # e.g. "0x1000000..."
            digits = parts[2]         # e.g. "25"
            cc = int(cc_label[2:])
            bits = hex_to_bits(root_hex)
            writer.writerow([cc, root_hex, digits, bits])
            count += 1
            if limit and count >= limit:
                break
    if skipped:
        print(
            f"ERROR: {skipped} malformed line(s) skipped — review input file",
            file=sys.stderr,
        )
        sys.exit(1)
    return count


def main():
    parser = argparse.ArgumentParser(
        description="Convert raw CC roots file to normalized CSV."
    )
    parser.add_argument("input", help="Raw roots file (e.g. CC_x.txt)")
    parser.add_argument("output", help="Output CSV path")
    parser.add_argument(
        "--limit", type=int, default=None, help="Stop after N rows"
    )
    args = parser.parse_args()
    n = convert(args.input, args.output, args.limit)
    print(f"Wrote {n} rows to {args.output}", file=sys.stderr)


if __name__ == "__main__":
    main()
