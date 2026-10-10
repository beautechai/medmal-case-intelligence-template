# evidence/: evidence index and certified-record request tracker

## Evidence index (`evidence_index.csv`)
Every document, photo, email, letter, audit log or recording gets a `doc_id` used everywhere else in this repo. Record where the file lives (in `data/private/`, never committed) and its **SHA-256 hash** so you can later show it hasn't changed.

```bash
sha256sum data/private/somefile.pdf      # Linux
shasum -a 256 data/private/somefile.pdf  # macOS
certutil -hashfile somefile.pdf SHA256   # Windows
```

## Certified-record request tracker (`record_requests.csv`)
One row per request: **requested → sent → due → received → certified → gaps**.
- Keep proof of sending (certified mail receipt, fax confirmation, portal screenshot).
- Under HIPAA (45 CFR 164.524), covered entities generally must act on access requests within 30 days (one 30-day extension with written notice). California H&S Code § 123110 has its own (often shorter) timelines for patient inspection and copies. Verify current rules with counsel.
- Ask for a **custodian of records declaration/certification** that the production is complete.
- After receipt, run `../records/completeness_checklist.md` and put gaps in `gaps_identified`; open a follow-up request for each gap.
- `status`: `open`, `partial`, `complete`, `overdue`, `escalated`.

Examples (fictional): `evidence_index_EXAMPLE.csv`, `record_requests_EXAMPLE.csv`.
