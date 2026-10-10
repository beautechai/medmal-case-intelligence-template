#!/usr/bin/env python3
"""Lab timeline across facilities with gap detection.

Reads a labs CSV (see schema/labs.schema.json), charts chosen analytes over time
with clinical event markers, and reports, per analyte, the calendar days with
no draws inside the observed window.

NOT MEDICAL OR LEGAL ADVICE. A "gap" only means no result appears in the data
you entered; it may reflect missing records rather than missing care.

Example:
    python3 labs/lab_timeline.py labs/example/labs_EXAMPLE.csv \
        --analytes WBC Hemoglobin Creatinine \
        --events labs/example/events_EXAMPLE.csv --out out/labs_EXAMPLE.png
"""
import argparse
import os
import sys

import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.dates as mdates  # noqa: E402


def load_labs(path):
    df = pd.read_csv(path, dtype=str).fillna("")
    required = {"facility", "collected_date", "analyte", "value"}
    missing = required - set(df.columns)
    if missing:
        sys.exit(f"ERROR: {path} is missing columns: {sorted(missing)}")
    df["collected_time"] = df.get("collected_time", "").replace("", "00:00")
    df["ts"] = pd.to_datetime(df["collected_date"] + " " + df["collected_time"], errors="coerce")
    bad = df["ts"].isna().sum()
    if bad:
        print(f"WARNING: {bad} row(s) with unparseable date/time were skipped", file=sys.stderr)
    df = df.dropna(subset=["ts"]).copy()
    df["value_num"] = pd.to_numeric(df["value"], errors="coerce")
    for c in ("ref_low", "ref_high"):
        df[c] = pd.to_numeric(df[c], errors="coerce") if c in df.columns else float("nan")
    df["day"] = df["ts"].dt.normalize()
    return df


def find_gaps(df, analytes, start=None, end=None):
    """Return {analyte: [list of (gap_start, gap_end, n_days)]} of days with no draws."""
    start = pd.Timestamp(start) if start else df["day"].min()
    end = pd.Timestamp(end) if end else df["day"].max()
    all_days = pd.date_range(start, end, freq="D")
    out = {}
    for a in analytes:
        have = set(df.loc[df["analyte"] == a, "day"])
        missing = [d for d in all_days if d not in have]
        runs, run = [], []
        for d in missing:
            if run and (d - run[-1]).days != 1:
                runs.append(run)
                run = []
            run.append(d)
        if run:
            runs.append(run)
        out[a] = [(r[0], r[-1], len(r)) for r in runs]
    return out, start, end


def plot(df, analytes, events, out_path, title):
    n = len(analytes)
    fig, axes = plt.subplots(n, 1, figsize=(11, 2.6 * n + 0.8), sharex=True, squeeze=False)
    facilities = sorted(df["facility"].unique())
    markers = ["o", "s", "^", "D", "v", "P", "X"]
    for i, a in enumerate(analytes):
        ax = axes[i][0]
        sub = df[(df["analyte"] == a) & df["value_num"].notna()].sort_values("ts")
        if sub.empty:
            ax.text(0.5, 0.5, f"No numeric data for {a}", transform=ax.transAxes, ha="center")
        ax.plot(sub["ts"], sub["value_num"], color="0.6", lw=1, zorder=1)
        for j, fac in enumerate(facilities):
            fs = sub[sub["facility"] == fac]
            if not fs.empty:
                ax.scatter(fs["ts"], fs["value_num"], marker=markers[j % len(markers)], s=28, zorder=2, label=fac)
        lo, hi = sub["ref_low"].dropna(), sub["ref_high"].dropna()
        if not lo.empty and not hi.empty:
            ax.axhspan(lo.median(), hi.median(), color="tab:green", alpha=0.08, label="ref range")
        unit = sub["unit"].iloc[0] if "unit" in sub.columns and not sub.empty else ""
        ax.set_ylabel(f"{a}\n{unit}")
        ax.grid(alpha=0.3)
        if events is not None:
            for _, ev in events.iterrows():
                ax.axvline(ev["date"], color="tab:red", ls="--", lw=0.9, alpha=0.7)
                if i == 0:
                    ax.annotate(ev["label"], (ev["date"], 1.0), xycoords=("data", "axes fraction"),
                                rotation=30, fontsize=7, va="bottom", ha="left", color="tab:red")
    axes[0][0].legend(fontsize=7, loc="upper right")
    axes[-1][0].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    fig.autofmt_xdate()
    fig.suptitle(title, y=0.995)
    fig.tight_layout()
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("labs_csv")
    p.add_argument("--analytes", nargs="+", help="Analytes to chart (default: all)")
    p.add_argument("--events", help="CSV with date,label[,category] for vertical markers")
    p.add_argument("--start", help="Window start YYYY-MM-DD for gap detection (default: first draw)")
    p.add_argument("--end", help="Window end YYYY-MM-DD (default: last draw)")
    p.add_argument("--out", default="out/lab_timeline.png", help="Chart output path (png/svg/pdf)")
    p.add_argument("--report", help="Optional path to write the gap report as Markdown")
    p.add_argument("--title", default="Lab timeline")
    args = p.parse_args(argv)

    df = load_labs(args.labs_csv)
    analytes = args.analytes or sorted(df["analyte"].unique())
    unknown = [a for a in analytes if a not in set(df["analyte"])]
    if unknown:
        print(f"WARNING: analytes not found in data: {unknown}", file=sys.stderr)

    events = None
    if args.events:
        events = pd.read_csv(args.events, dtype=str).fillna("")
        events["date"] = pd.to_datetime(events["date"], errors="coerce")
        events = events.dropna(subset=["date"])

    plot(df, analytes, events, args.out, args.title)

    gaps, start, end = find_gaps(df, analytes, args.start, args.end)
    lines = [f"# Days with no draws per analyte ({start.date()} to {end.date()})", "",
             "Facilities in data: " + ", ".join(sorted(df["facility"].unique())), ""]
    for a in analytes:
        n_draw_days = df.loc[df["analyte"] == a, "day"].nunique()
        total = sum(g[2] for g in gaps[a])
        lines.append(f"## {a}: {n_draw_days} day(s) with draws, {total} day(s) without")
        if not gaps[a]:
            lines.append("- no gaps")
        for s, e, n in gaps[a]:
            span = f"{s.date()}" if n == 1 else f"{s.date()} to {e.date()}"
            lines.append(f"- {span} ({n} day{'s' if n != 1 else ''})")
        lines.append("")
    lines.append("Note: a gap means no result in YOUR data. Check whether records are missing before drawing conclusions.")
    report = "\n".join(lines)
    print(report)
    print(f"\nChart written to {args.out}")
    if args.report:
        os.makedirs(os.path.dirname(args.report) or ".", exist_ok=True)
        with open(args.report, "w") as f:
            f.write(report + "\n")


if __name__ == "__main__":
    main()
