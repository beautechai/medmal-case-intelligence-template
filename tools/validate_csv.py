#!/usr/bin/env python3
"""Lightweight CSV validator against the JSON Schemas in schema/ (standard library only).

Checks: header columns present, required fields non-empty, enum values,
YYYY-MM-DD date patterns, numeric types.

    python3 tools/validate_csv.py labs/example/labs_EXAMPLE.csv schema/labs.schema.json
    python3 tools/validate_csv.py --examples      # validate all *_EXAMPLE.csv files
"""
import csv
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXAMPLES = {
    "records/inventory_EXAMPLE.csv": "records_inventory",
    "labs/example/labs_EXAMPLE.csv": "labs",
    "labs/example/events_EXAMPLE.csv": "lab_events",
    "medications/medications_EXAMPLE.csv": "medications",
    "procedures/procedures_EXAMPLE.csv": "procedures",
    "events/events_EXAMPLE.csv": "events",
    "social-media/social_media_review_EXAMPLE.csv": "social_media_review",
    "evidence/evidence_index_EXAMPLE.csv": "evidence_index",
    "evidence/record_requests_EXAMPLE.csv": "record_requests",
}


def validate(csv_path, schema_path):
    schema = json.load(open(schema_path))
    props, required = schema["properties"], schema.get("required", [])
    errors = []
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        missing = [c for c in props if c not in (reader.fieldnames or [])]
        if missing:
            errors.append(f"missing columns: {missing}")
        for i, row in enumerate(reader, start=2):
            for col, spec in props.items():
                v = (row.get(col) or "").strip()
                if col in required and not v:
                    errors.append(f"line {i}: '{col}' is required")
                if not v:
                    continue
                if "enum" in spec and v not in spec["enum"]:
                    errors.append(f"line {i}: '{col}'={v!r} not in {spec['enum'][:-1]}")
                if "pattern" in spec and not re.match(spec["pattern"], v):
                    errors.append(f"line {i}: '{col}'={v!r} should be YYYY-MM-DD")
                t = spec.get("type")
                if isinstance(t, list) and ("number" in t or "integer" in t):
                    try:
                        int(v) if "integer" in t else float(v)
                    except ValueError:
                        errors.append(f"line {i}: '{col}'={v!r} is not a {t[0]}")
    return errors


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "--examples":
        pairs = [(os.path.join(ROOT, c), os.path.join(ROOT, "schema", s + ".schema.json")) for c, s in EXAMPLES.items()]
    elif len(sys.argv) == 3:
        pairs = [(sys.argv[1], sys.argv[2])]
    else:
        sys.exit(__doc__)
    bad = 0
    for c, s in pairs:
        errs = validate(c, s)
        print(f"{'OK  ' if not errs else 'FAIL'} {os.path.relpath(c, ROOT)}")
        for e in errs:
            print("     " + e)
        bad += bool(errs)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
