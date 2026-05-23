#!/usr/bin/env python3
"""VAULT — DeFi yield optimizer — APY router with IL adjustment."""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

CONFIG = json.loads(Path(__file__).parent.joinpath("config.json").read_text())


def core_compute(data: dict) -> dict:
    """Core algorithm. Rank protocols by net APY after fees and IL estimate."""
    
    pools = data.get("pools", [])
    ranked = []
    for p in pools:
        apr = p.get("apr", 0)
        n = p.get("compound_per_year", 365)
        apy = (1 + apr / n) ** n - 1
        fee = p.get("performance_fee_pct", 0.1)
        net = apy * (1 - fee)
        ranked.append({"pool": p.get("name"), "apy": round(apy, 4), "net_apy": round(net, 4)})
    ranked.sort(key=lambda x: -x["net_apy"])
    result = {"top": ranked[:10]}
    return result


def main():
    ap = argparse.ArgumentParser(description="VAULT")
    ap.add_argument("input", nargs="?", help="JSON input file")
    ap.add_argument("--output", default="-", help="output path or '-'")
    args = ap.parse_args()

    if args.input:
        data = json.loads(Path(args.input).read_text())
    else:
        data = json.loads(sys.stdin.read())

    result = core_compute(data)
    out_text = json.dumps(result, indent=2)
    if args.output == "-":
        print(out_text)
    else:
        Path(args.output).write_text(out_text)


if __name__ == "__main__":
    main()
