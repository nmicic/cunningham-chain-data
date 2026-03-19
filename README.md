# Cunningham Chain Dataset

First-kind Cunningham chain roots (CC10 through CC18) from the 2026 search campaign.

## What this repo contains

| Path | Description |
|------|-------------|
| `sample/cc10plus_roots_sample_1000.txt` | First 1000 roots (raw text format) |
| `sample/cc10plus_roots_sample_1000.csv` | Same 1000 roots (normalized CSV) |
| `scripts/make_snapshot_csv.py` | Converts raw text to normalized CSV |
| `manifest/dataset_manifest.json` | Snapshot metadata and counts |
| `schema/README.md` | Format documentation for both raw and CSV |

## Getting the data

- `git clone` gives you schema, manifest, samples, and scripts.
- Full snapshots are on the [GitHub release page](https://github.com/nmicic/cunningham-chain-data/releases).
- Latest aggregate snapshot: [v2026-03-19-snapshot](https://github.com/nmicic/cunningham-chain-data/releases/tag/v2026-03-19-snapshot).
- Earlier March 12 snapshot remains available separately, including the raw text asset.

## Full dataset

The current aggregate snapshot is available as a [GitHub Release asset](https://github.com/nmicic/cunningham-chain-data/releases/tag/v2026-03-19-snapshot) (not tracked in git):

| Asset | Download | Uncompressed | Format |
|-------|----------|--------------|--------|
| `cc10plus_roots_snapshot_2026-03-19.csv.gz` | 19 MB | 55 MB | `cc,root_hex,digits,bits` |

This March 19 release is cumulative, not a delta. It is published as a normalized CSV and includes the two first-kind CC18 roots found after the first release.

## Snapshot summary

| CC level | Count |
|----------|------:|
| CC10 | 1,262,271 |
| CC11 | 225,422 |
| CC12 | 52,296 |
| CC13 | 9,467 |
| CC14 | 1,674 |
| CC15 | 295 |
| CC16 | 55 |
| CC17 | 7 |
| CC18 | 2 |
| **Total** | **1,551,489** |

Bit range: 64-153. Primary search band: 87-90 bits.

The earlier March 12 release remains on the releases page for anyone who wants the original raw text snapshot.

## Generating the CSV

The latest release is already published as normalized CSV. `scripts/make_snapshot_csv.py` remains here for converting the earlier raw text format or future raw snapshots.

## Related

- Main code repo: [cunningham-chain-search](https://github.com/nmicic/cunningham-chain-search) - search engine, analysis scripts, visualizations
- [Cunningham chain tables (pzktupel.de)](https://www.pzktupel.de/CC/cc.php)

## Author

Nenad Micic, Belgium - [LinkedIn](https://be.linkedin.com/in/nenadmicic)

## License

See [LICENSE](LICENSE).
