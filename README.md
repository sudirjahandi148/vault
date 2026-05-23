# VAULT

> DeFi yield optimizer — APY router with IL adjustment

A focused, single-purpose tool. DeFi yield optimizer — APY router with IL adjustment

## Demo

[Live demo](https://sudirjahandi148.github.io/vault/)

## Quick start

```bash
git clone https://github.com/sudirjahandi148/vault
cd vault
pip install -r requirements.txt
python main.py sample_input.jsonl
```

## Why

DefiLlama yields page bagus tapi info-nya snapshot, ga kasih historical APY trend atau IL-adjusted return. Mau decide masuk pool mana harus cross-ref 5 tab.

VAULT aku build buat solve itu — fokus di LP fee maximizer. Pendekatannya bukan rule-based atau heuristic kasar, tapi proper math. Aave utilization curve: borrow_APR = base + (util / kink) * slope1 if util ≤ kink, else base + slope1 + (util - kink) / (1 - kink) * slope2. Supply APY = borrow_APR * util * (1 - reserve_factor).

Output format: Allocation suggestion CSV: from_protocol, to_protocol, asset, amount, expected_gain_30d, gas_cost, 

## How it works

Rank protocols by net APY after fees and IL estimate.

## Output format

```json
{
  "result": "see core_compute output"
}
```

## Tunables

See `config.json` for runtime parameters.

## Limitations

- MVP scope, single-protocol focus per run.
- No persistent state — input/output flow only.

## License

MIT
