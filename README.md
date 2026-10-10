# medmal-case-intelligence-template

An open-source, fill-in-the-blanks workspace for **patients, families and patient advocates** who are organizing a possible medical-malpractice matter and want to build a structured "case intelligence layer": an inventory of records, completeness checks, lab/medication/procedure timelines, deadline awareness, an event log, a social-media risk review, an evidence index, and a master timeline your attorney can read in minutes.

Everything here is **generic**. All sample data is **fictional and labeled `EXAMPLE`**. There are no real patients, clinicians, facilities or dates in this repository.

---

> ## ⚠️ NOT LEGAL OR MEDICAL ADVICE
>
> This template is an organizational aid only. It is **not legal advice, not medical advice**, and it does not create an attorney-client or provider-patient relationship. Laws differ by state and change over time; the California material here may be outdated or may not apply to your facts.
>
> **Consult a licensed attorney in your state promptly. Malpractice deadlines are short** (in California, as little as **one year** from when you first suspected wrongdoing, and only **six months** for a claim against a public entity). Do not let organizing your records delay a consultation. Many malpractice attorneys offer free initial consultations.

---

> ## 🔒 PRIVACY WARNING: never commit real health information to a public repo
>
> - **Do not put real names, dates of birth, MRNs, record pages, photos, recordings or any protected health information (PHI) in a public fork.** Anything pushed to a public GitHub repo should be assumed copied forever, even if you delete it later.
> - **Use a private copy.** Click **"Use this template" → "Create a new repository" → Private**, or keep everything offline on your own computer.
> - The `.gitignore` excludes `data/private/`, `*.pdf`, images, audio and video by default. Keep raw records in `data/private/`. Check `git status` before every commit.
> - Your attorney may want to control how work product is created and shared. Ask them before sharing this workspace with anyone, including friends, support groups or online forums.

---

## What's inside

| Folder | Purpose |
|---|---|
| `schema/` | JSON Schema + CSV header definitions for every table, so tools and spreadsheets agree |
| `records/` | Records inventory, completeness checklist, EHR audit-trail / access-log request guide |
| `labs/` | Multi-facility lab timeline template, gap detection and charting script, fictional example |
| `medications/` | Ordered / given (MAR) / held / discontinued timeline with who and when |
| `procedures/` | Incisions, wound VAC, ostomy, complications, consent, op-note filing time vs. date of service |
| `deadlines/` | California CCP § 340.5 calculator with CCP § 364 and Government Claims Act notes, verified case citations |
| `events/` | Intimidation and conflict-of-interest event log, with HIPAA / H&S Code § 1278.5 / Penal Code § 632 notes |
| `social-media/` | Ranked-risk review template and an anti-spoliation warning |
| `evidence/` | Evidence index plus certified-record request tracker |
| `tools/` | `build_timeline.py` merges the section CSVs into one Markdown master timeline; `validate_csv.py` checks CSVs against the schemas |

## Quickstart

1. **Make a private copy.** On GitHub use **Use this template → Private**, or download the ZIP and work offline.
2. **Set up Python** (3.9+):
   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Run the examples** to see how everything fits together:
   ```bash
   # Lab chart + days-without-draws report
   python3 labs/lab_timeline.py labs/example/labs_EXAMPLE.csv \
       --analytes WBC Hemoglobin Creatinine \
       --events labs/example/events_EXAMPLE.csv --out out/labs_EXAMPLE.png

   # California deadline calculator (fictional dates)
   python3 deadlines/ca_340_5_calculator.py --injury 2030-03-01 --discovery 2030-05-15

   # Master timeline from all section CSVs
   python3 tools/build_timeline.py --mode example --out out/MASTER_TIMELINE_EXAMPLE.md

   # Check CSVs against the schemas
   python3 tools/validate_csv.py --examples
   ```
4. **Start your own case** in your private copy:
   - Create `data/private/` (git-ignored) for raw PDFs, images and exports.
   - Copy each `*_TEMPLATE.csv` to a new file without `TEMPLATE` (for example `records/inventory.csv`) and fill it in.
   - Work through `records/completeness_checklist.md` and send the requests in `records/audit_trail_request_guide.md`.
   - Run `deadlines/ca_340_5_calculator.py` **and then confirm every date with an attorney.**
   - Re-run `tools/build_timeline.py` whenever you add rows.

## Folder structure

```
medmal-case-intelligence-template/
├── README.md
├── LICENSE                         MIT
├── CONTRIBUTING.md
├── requirements.txt
├── .gitignore                      excludes data/private/, *.pdf, images, audio, video
├── schema/
│   ├── README.md
│   ├── csv_headers.md
│   └── *.schema.json               one JSON Schema per table
├── records/
│   ├── README.md
│   ├── inventory_TEMPLATE.csv
│   ├── inventory_EXAMPLE.csv
│   ├── completeness_checklist.md
│   └── audit_trail_request_guide.md
├── labs/
│   ├── README.md
│   ├── labs_TEMPLATE.csv
│   ├── lab_events_TEMPLATE.csv
│   ├── lab_timeline.py
│   └── example/
│       ├── labs_EXAMPLE.csv
│       └── events_EXAMPLE.csv
├── medications/
│   ├── README.md
│   ├── medications_TEMPLATE.csv
│   └── medications_EXAMPLE.csv
├── procedures/
│   ├── README.md
│   ├── procedures_TEMPLATE.csv
│   └── procedures_EXAMPLE.csv
├── deadlines/
│   ├── README.md                   statutes, verified case law, tolling, estoppel
│   └── ca_340_5_calculator.py
├── events/
│   ├── README.md                   HIPAA, H&S 1278.5, Penal Code 632 notes
│   ├── events_TEMPLATE.csv
│   └── events_EXAMPLE.csv
├── social-media/
│   ├── README.md                   spoliation warning
│   ├── social_media_review_TEMPLATE.csv
│   └── social_media_review_EXAMPLE.csv
├── evidence/
│   ├── README.md
│   ├── evidence_index_TEMPLATE.csv
│   ├── evidence_index_EXAMPLE.csv
│   ├── record_requests_TEMPLATE.csv
│   └── record_requests_EXAMPLE.csv
└── tools/
    ├── README.md
    ├── build_timeline.py
    └── validate_csv.py
```

## Conventions

- **Dates** are ISO 8601: `YYYY-MM-DD`, times `HH:MM` (24-hour, the facility's local time).
- **Every fact gets a source**: `source_doc_id` + `page` (or Bates number) pointing to the evidence index, so anyone can verify it.
- **Separate fact from interpretation**: put what the record says in `description` and your questions for counsel in `notes`.
- **People are referenced by role** (e.g., "RN-1", "Surgeon-A") in shared copies; keep a private key mapping roles to names in `data/private/`.
- Files ending in `_EXAMPLE` are fictional demo data. Delete or ignore them in your own copy.

## License

MIT. See `LICENSE`. Contributions welcome. See `CONTRIBUTING.md`.
