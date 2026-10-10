# procedures/: procedure, wound and documentation timeline

One row per procedure or related event. Categories: `incision`, `wound_vac_placement`, `wound_vac_change`, `ostomy`, `complication`, `consent`, `op_note`, `anesthesia`, `other`.

Capture:
- **Incisions**: site and extent (length/depth as documented); compare op note, nursing wound assessments and photos.
- **Wound VAC**: placement, every dressing change, settings, who performed it; missed or late changes.
- **Ostomy**: creation, site marking, complications, revisions.
- **Complications**: returns to OR, bleeding, infection, dehiscence, with times.
- **Consent**: when signed vs. when the procedure began; who obtained it; whether the procedure performed matches the consent.
- **Op-note filing time vs. date of service**: `note_signed_datetime` and `note_filed_datetime` (from the audit trail) vs. `date_of_service`/`end_time`. `filing_lag_hours` = hours from procedure end to filing. Long lags and addenda after a complication are questions for counsel.

Template: `procedures_TEMPLATE.csv` · Example (fictional): `procedures_EXAMPLE.csv` · Schema: `../schema/procedures.schema.json`.
