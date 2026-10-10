# schema/

One JSON Schema (draft 2020-12) per table. Each CSV row is validated as one object; all values are strings in CSV, with dates as `YYYY-MM-DD` and numeric columns parseable as numbers.

| Schema | CSV template |
|---|---|
| `records_inventory.schema.json` | `records/inventory_TEMPLATE.csv` |
| `labs.schema.json` | `labs/labs_TEMPLATE.csv` |
| `lab_events.schema.json` | `labs/lab_events_TEMPLATE.csv` |
| `medications.schema.json` | `medications/medications_TEMPLATE.csv` |
| `procedures.schema.json` | `procedures/procedures_TEMPLATE.csv` |
| `events.schema.json` | `events/events_TEMPLATE.csv` |
| `social_media_review.schema.json` | `social-media/social_media_review_TEMPLATE.csv` |
| `evidence_index.schema.json` | `evidence/evidence_index_TEMPLATE.csv` |
| `record_requests.schema.json` | `evidence/record_requests_TEMPLATE.csv` |

Header lines for every table: `csv_headers.md`. Column descriptions are in each schema's `description` fields. Validate with `python3 tools/validate_csv.py`.

Shared conventions: every fact row should carry `source_doc_id` + `page` pointing to `evidence/evidence_index.csv`; people are referenced by **role placeholders** (e.g. `RN-1`, `Surgeon-A`) in anything you might share.
