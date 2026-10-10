# medications/: medication timeline

One row per **action** on a medication: `ordered`, `verified`, `given`, `held`, `refused`, `not_given`, `discontinued`, `changed`. Rows sharing a `med_id` belong to the same order, so you can see each order's life cycle.

Sources: physician orders, pharmacy verification, the **MAR** (medication administration record), automated dispensing cabinet override reports, nursing notes, discharge med reconciliation.

What to look for (questions for counsel/expert, not conclusions):
- ordered but never given, or given late vs. the ordered time/frequency;
- doses **held** without a documented reason or without notifying the prescriber;
- discontinuations with no documented reason or order;
- antibiotics, anticoagulants, insulin, opioids/sedatives, pressors: timing relative to lab changes and events;
- medication changes across a transfer (reconciliation gaps).

Record **who** by role/placeholder (`RN-1`, `Hospitalist-A`) in shared copies; keep the name key in `data/private/`.

Template: `medications_TEMPLATE.csv` · Example (fictional): `medications_EXAMPLE.csv` · Schema: `../schema/medications.schema.json`.
