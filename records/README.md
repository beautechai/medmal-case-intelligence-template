# records/: intake and completeness checking

1. **Inventory** every file you receive in `inventory.csv` (copy `inventory_TEMPLATE.csv`; see `inventory_EXAMPLE.csv`). One row per document or production set. Keep the files themselves in `data/private/` (git-ignored).
2. **Check completeness** with `completeness_checklist.md`. Most record sets are incomplete the first time.
3. **Request the EHR audit trail / access log** using `audit_trail_request_guide.md`. It shows who created, edited, viewed and signed each note, and when.
4. Track every request and its status in `../evidence/record_requests.csv`.

Schema: `../schema/records_inventory.schema.json`.

Tips
- Never write on, highlight, rename inside, or re-save original files. Work from copies; keep originals read-only and record a SHA-256 hash in `../evidence/evidence_index.csv` (`sha256sum file.pdf` on Linux/macOS, `certutil -hashfile file.pdf SHA256` on Windows).
- Note **how** you received each set (portal download, paper copy, certified production, subpoena). Different channels often contain different content. Cross-check them.
