# Contributing

Thanks for helping patients and advocates get organized. Contributions of templates, checklists, scripts, other states' deadline notes, and translations are welcome.

## The one rule: no real personal data. Ever.

- **Never include real names, dates, record excerpts, images, recordings, case numbers or any protected health information** in issues, pull requests, examples or test data, even "anonymized." Re-identification is easier than it looks.
- Example data must be **clearly fictional and labeled `EXAMPLE`** (use the made-up facilities "EXAMPLE General Hospital" / "EXAMPLE Rehab Center", role placeholders like `RN-1`, and dates in the future, e.g. 2030).
- PRs containing anything that looks like real personal data will be closed and the content removed.
- Do not describe your own case in issues. Ask your attorney instead.

## Legal content

- This project is **not legal advice**. Keep disclaimers prominent.
- Every statute or case citation must include a **verifiable source link** (official legislature site, court site, Justia, etc.) and you must have read the source. Unverifiable citations will be removed.
- Note the jurisdiction and the date you verified it. Prefer adding new states as separate files (e.g. `deadlines/README.<state>.md`) rather than changing California material.

## Code

- Python 3.9+. Keep dependencies minimal (standard library, pandas, matplotlib).
- Scripts must run on the bundled `EXAMPLE` data:
  ```bash
  python3 tools/validate_csv.py --examples
  python3 tools/build_timeline.py --mode example --out out/MASTER_TIMELINE_EXAMPLE.md
  python3 labs/lab_timeline.py labs/example/labs_EXAMPLE.csv --events labs/example/events_EXAMPLE.csv --out out/labs.png
  python3 deadlines/ca_340_5_calculator.py --injury 2030-03-01 --discovery 2030-05-15
  ```
- If you change a table, update its JSON Schema, `*_TEMPLATE.csv`, `schema/csv_headers.md`, and any affected example and script.
- Deadline logic should err on the side of the **earlier** date.

## Process

1. Fork, branch, make your change.
2. Run the commands above.
3. Open a PR describing what changed and how you verified any legal citation.

By contributing you agree your contribution is licensed under the MIT License.
