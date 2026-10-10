#!/usr/bin/env python3
"""Build a master timeline (Markdown) from the section CSVs.

Reads, if present:
  records/inventory.csv              (received documents)
  labs/labs.csv                      (abnormal-flagged results only, by default)
  labs/lab_events.csv
  medications/medications.csv
  procedures/procedures.csv
  events/events.csv
  social-media/social_media_review.csv
  evidence/record_requests.csv

--mode example  uses the *_EXAMPLE.csv files instead (fictional demo data)
--mode case     uses your own files (names above)
--mode auto     (default) uses your files if any exist, otherwise the examples

Standard library only. Output: one chronological Markdown table with a source
column so every entry can be verified.
"""
import argparse
import csv
import glob
import os
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECTIONS = {
    "records": "records/inventory",
    "labs": "labs/labs",
    "lab_events": "labs/lab_events",
    "medications": "medications/medications",
    "procedures": "procedures/procedures",
    "events": "events/events",
    "social": "social-media/social_media_review",
    "requests": "evidence/record_requests",
}
EXAMPLE_OVERRIDES = {"labs": "labs/example/labs_EXAMPLE.csv", "lab_events": "labs/example/events_EXAMPLE.csv"}


def path_for(key, mode):
    if mode == "example":
        return os.path.join(ROOT, EXAMPLE_OVERRIDES.get(key, SECTIONS[key] + "_EXAMPLE.csv"))
    return os.path.join(ROOT, SECTIONS[key] + ".csv")


def read(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8-sig") as f:
        return [{k: (v or "").strip() for k, v in r.items() if k} for r in csv.DictReader(f)]


def src(r):
    s = r.get("source_doc_id") or r.get("evidence_doc_id") or r.get("doc_id") or ""
    if r.get("page"):
        s += f" p.{r['page']}"
    return s


def esc(s):
    return (s or "").replace("|", "\\|").replace("\n", " ")


def collect(mode, all_labs):
    items = []

    def add(date, time, section, text, source="", rid=""):
        if date:
            items.append((date, time or "", section, text, source, rid))

    for r in read(path_for("records", mode)):
        add(r.get("received_date"), "", "records",
            f"Received {r.get('doc_type','')} from {r.get('facility','')} ({r.get('source_type','')}, "
            f"{r.get('page_count','?')} pp)" + (f"; {r['notes']}" if r.get("notes") else ""), r.get("doc_id"), r.get("doc_id"))
    labs = read(path_for("labs", mode))
    for r in labs:
        if all_labs or r.get("flag"):
            add(r.get("collected_date"), r.get("collected_time"), "labs",
                f"{r.get('analyte')} {r.get('value')} {r.get('unit','')} [{r.get('flag') or 'normal'}] @ {r.get('facility')}",
                src(r))
    for r in read(path_for("lab_events", mode)):
        add(r.get("date"), "", "clinical event", f"{r.get('label')} ({r.get('category','')})")
    for r in read(path_for("medications", mode)):
        add(r.get("action_date"), r.get("action_time"), "medications",
            f"{r.get('action','').upper()}: {r.get('medication')} {r.get('dose','')} {r.get('route','')} "
            f"{r.get('frequency','')} by {r.get('actor_role','?')}" + (f"; reason: {r['reason']}" if r.get("reason") else ""),
            src(r), r.get("med_id"))
    for r in read(path_for("procedures", mode)):
        lag = f"; note filed {r['note_filed_datetime']} (lag {r['filing_lag_hours']} h)" if r.get("note_filed_datetime") else ""
        add(r.get("date_of_service"), r.get("start_time"), "procedures",
            f"[{r.get('category')}] {r.get('procedure')} {('at ' + r['site']) if r.get('site') else ''} "
            f"{('(' + r['extent'] + ')') if r.get('extent') else ''} by {r.get('performed_by_role','?')}{lag}",
            src(r), r.get("proc_id"))
    for r in read(path_for("events", mode)):
        mis = " [ROLE MISIDENTIFIED]" if r.get("role_misidentified") == "Y" else ""
        add(r.get("date"), r.get("time"), "events",
            f"[{r.get('category')}]{mis} {r.get('person_role','')}: {r.get('description','')}", src(r), r.get("event_id"))
    for r in read(path_for("social", mode)):
        add(r.get("post_date"), "", "social media",
            f"{r.get('platform')} post (risk {r.get('risk_rank','?')}): {r.get('content_summary','')}", "", r.get("post_id"))
    for r in read(path_for("requests", mode)):
        rid = r.get("request_id")
        what = f"{r.get('facility')} / {r.get('department','')}: {r.get('records_requested','')}"
        add(r.get("sent_date"), "", "record request", f"SENT {what}", "", rid)
        add(r.get("due_date"), "", "record request", f"DUE {what}", "", rid)
        add(r.get("received_date"), "", "record request",
            f"RECEIVED {what} ({r.get('pages_received','?')} pp, certified={r.get('certified','?')})"
            + (f"; gaps: {r['gaps_identified']}" if r.get("gaps_identified") else ""), "", rid)
    items.sort(key=lambda x: (x[0], x[1] or "99:99"))
    return items


def has_case_files():
    return any(os.path.exists(path_for(k, "case")) for k in SECTIONS)


def main(argv=None):
    p = argparse.ArgumentParser(description="Build a Markdown master timeline from section CSVs.")
    p.add_argument("--mode", choices=["auto", "case", "example"], default="auto")
    p.add_argument("--out", default="out/MASTER_TIMELINE.md")
    p.add_argument("--all-labs", action="store_true", help="include normal lab results too")
    a = p.parse_args(argv)
    mode = a.mode if a.mode != "auto" else ("case" if has_case_files() else "example")
    items = collect(mode, a.all_labs)
    if not items:
        sys.exit(f"No rows found (mode={mode}). Copy *_TEMPLATE.csv files and fill them in.")
    title = "Master timeline" + (" (EXAMPLE, fictional data)" if mode == "example" else "")
    counts = Counter(i[2] for i in items)
    lines = [f"# {title}", "",
             "> Generated by tools/build_timeline.py. Not legal or medical advice. Verify each entry against its source.",
             "> CONFIDENTIAL if built from real records: do not commit to a public repository.", "",
             f"Entries: {len(items)} (" + ", ".join(f"{k}: {v}" for k, v in sorted(counts.items())) + ")",
             f"Range: {items[0][0]} to {items[-1][0]}", "",
             "| Date | Time | Section | Entry | Source | ID |", "|---|---|---|---|---|---|"]
    for d, t, s, txt, source, rid in items:
        lines.append(f"| {d} | {t} | {s} | {esc(' '.join(txt.split()))} | {esc(source)} | {esc(rid)} |")
    out = a.out if os.path.isabs(a.out) else os.path.join(os.getcwd(), a.out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote {len(items)} entries ({mode} mode) to {a.out}")


if __name__ == "__main__":
    main()
