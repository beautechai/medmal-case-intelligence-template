# tools/

| Script | What it does |
|---|---|
| `build_timeline.py` | Merges all section CSVs into one chronological Markdown table (`out/MASTER_TIMELINE.md`) with a source column. Standard library only. |
| `validate_csv.py` | Checks a CSV against its JSON Schema in `../schema/` (columns, required fields, enums, dates, numbers). Standard library only. |

```bash
python3 tools/build_timeline.py --mode example --out out/MASTER_TIMELINE_EXAMPLE.md
python3 tools/build_timeline.py --out out/MASTER_TIMELINE.md          # uses your own CSVs when present
python3 tools/build_timeline.py --all-labs                             # include normal lab values
python3 tools/validate_csv.py --examples
python3 tools/validate_csv.py medications/medications.csv schema/medications.schema.json
```

Your own CSVs use the template names without the suffix, e.g. `medications/medications.csv`, `labs/labs.csv`, `labs/lab_events.csv`, `evidence/record_requests.csv`.

`out/` is git-ignored. A timeline built from real records is confidential: never commit it to a public repo.
