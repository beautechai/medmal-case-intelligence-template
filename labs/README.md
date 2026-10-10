# labs/: lab timeline across facilities with gap detection

Put every lab result from every facility into one CSV (`labs.csv`, copied from `labs_TEMPLATE.csv`), one row per analyte result. Normalize analyte names (e.g. always `Hemoglobin`, not `Hgb`/`HGB`) so results from different facilities line up.

Optional: an events CSV (`lab_events_TEMPLATE.csv`: `date,label,category`) for surgeries, transfers and complications, drawn as vertical markers.

## Run

```bash
pip install -r requirements.txt
python3 labs/lab_timeline.py labs/example/labs_EXAMPLE.csv \
    --analytes WBC Hemoglobin Creatinine Lactate \
    --events labs/example/events_EXAMPLE.csv \
    --out out/labs_EXAMPLE.png --report out/lab_gaps_EXAMPLE.md
```

Output:
- a chart (one panel per analyte, marker shape per facility, shaded reference range, red dashed event lines);
- a report of **calendar days with no draws** per analyte within the window (first to last draw, or `--start/--end`).

The `example/` data is **fictional** (two made-up facilities, dates in 2030).

## Reading the gap report
A gap means there is **no result in your data**. Before treating it as missing care, check:
- whether the records you have are complete (`../records/completeness_checklist.md`);
- point-of-care tests (glucose, blood gases) that may be charted in flowsheets instead of the lab section;
- outside labs referenced in notes.

Then list the questions for counsel and your expert (e.g., "no lactate between X and Y despite fever"). Interpretation belongs to qualified medical experts.
