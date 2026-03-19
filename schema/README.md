# Dataset Schema

## Raw text format

One root per line:

```
CC<level> 0x<hex_root> <decimal_digits>
```

| Field | Description |
|-------|-------------|
| `CC<level>` | Chain length (e.g. `CC10`, `CC18`) |
| `0x<hex_root>` | Root prime in hexadecimal |
| `<decimal_digits>` | Number of decimal digits in the root |

Example lines:

```
CC10 0x100000088F309C70F2AEE1F 25
CC13 0x83E20E6FED56062713 20
CC18 0xB149165114F43BF4F72249 27
```

## Normalized CSV format

Columns:

| Column | Type | Description |
|--------|------|-------------|
| `cc` | int | Chain length (10, 11, ..., 18) |
| `root_hex` | string | Root prime as `0x`-prefixed hex |
| `digits` | int | Decimal digit count |
| `bits` | int | Bit length of the root |

Example row:

```csv
cc,root_hex,digits,bits
18,0xB149165114F43BF4F72249,27,88
```

## Notes

- All roots are first-kind Cunningham chains: p, 2p+1, 4p+3, ...
- The March 19, 2026 release is a cumulative aggregate snapshot, not a delta release.
- The latest public asset is a normalized CSV; the earlier March 12 release also includes a raw text snapshot.
- Derived analyses (gap statistics, immunization, ghost chains, twins, clusters) live in the main code repo: [cunningham-chain-search](https://github.com/nmicic/cunningham-chain-search)
