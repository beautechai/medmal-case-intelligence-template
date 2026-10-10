#!/usr/bin/env python3
"""California medical-malpractice deadline calculator (CCP 340.5 / 364 / Gov. Claims Act).

    *****************************************************************
    *  NOT LEGAL ADVICE.  ESTIMATES ONLY.  DEADLINES ARE SHORT.     *
    *  The date your claim "accrued" (when you suspected, or should *
    *  have suspected, wrongdoing) is a legal judgment that courts  *
    *  often decide AGAINST patients. Tolling, estoppel, minors,    *
    *  public entities, federal facilities and wrongful-death rules *
    *  can all change the answer. Talk to a licensed California     *
    *  attorney NOW and treat the EARLIEST date below as the real   *
    *  deadline unless your attorney tells you otherwise.           *
    *****************************************************************

Inputs
  --injury      date of injury (YYYY-MM-DD)
  --discovery   date you first discovered/suspected (or reasonably should have
                suspected) that the injury was caused by someone's wrongdoing
  --notice      (optional) date a CCP 364 notice of intent to sue was served
  --public-entity  include Government Claims Act notes (county/district/UC
                hospitals, public clinicians, etc.)
  --today       (optional) override today's date for "days remaining"
  --json        machine-readable output

Rules implemented (see deadlines/README.md for citations):
  * CCP 340.5: 3 years after injury OR 1 year after discovery, whichever first.
  * CCP 364(d) / Woods v. Young (1991) 53 Cal.3d 315: a 364(a) 90-day notice
    served during the LAST 90 days of the 1-year period tolls it 90 days.
  * Gov. Code 911.2 / 911.4 / 945.6: 6-month claim; late-claim application
    within 1 year; suit 6 months after written rejection (else 2 years).
"""
import argparse
import calendar
import datetime as dt
import json
import sys

BANNER = (
    "=" * 72 + "\n"
    "NOT LEGAL ADVICE - ESTIMATES ONLY - CONSULT A CALIFORNIA ATTORNEY PROMPTLY\n"
    "Treat the EARLIEST date as your deadline. Accrual/tolling are fact- and\n"
    "law-dependent and are frequently decided against patients.\n" + "=" * 72
)


def add_years(d, n):
    """Add n years; Feb 29 maps to Feb 28 (the conservative, earlier date)."""
    y = d.year + n
    if d.month == 2 and d.day == 29 and not calendar.isleap(y):
        return dt.date(y, 2, 28)
    return d.replace(year=y)


def add_months(d, n):
    """Add n calendar months; day clamps to month end (conservative)."""
    m0 = d.month - 1 + n
    y, m = d.year + m0 // 12, m0 % 12 + 1
    return dt.date(y, m, min(d.day, calendar.monthrange(y, m)[1]))


def parse(s, name):
    try:
        return dt.date.fromisoformat(s)
    except (TypeError, ValueError):
        sys.exit(f"ERROR: --{name} must be YYYY-MM-DD, got {s!r}")


def weekend_note(d):
    if d.weekday() >= 5:
        return (f"{d} falls on a {d.strftime('%A')}. CCP 12a may extend a deadline that lands on a "
                "weekend/court holiday to the next court day, but do not rely on that; file earlier.")
    return None


def compute(injury, discovery, notice=None, public_entity=False, today=None):
    if discovery < injury:
        print("WARNING: discovery date is before injury date; check inputs.", file=sys.stderr)
    one_year = add_years(discovery, 1)
    three_year = add_years(injury, 3)
    earliest = min(one_year, three_year)
    governing = "1-year (discovery)" if one_year <= three_year else "3-year (outside limit)"

    win_start = earliest - dt.timedelta(days=90)
    res = {
        "inputs": {"injury": injury, "discovery": discovery, "notice": notice, "public_entity": public_entity},
        "ccp_340_5": {
            "one_year_from_discovery": one_year,
            "three_years_from_injury": three_year,
            "earliest_deadline": earliest,
            "governing_period": governing,
        },
        "ccp_364": {
            "notice_window_start": win_start,
            "notice_window_end": earliest,
            "extended_deadline_if_served_in_window": earliest + dt.timedelta(days=90),
            "note": ("Per Woods v. Young (1991) 53 Cal.3d 315, a CCP 364(a) notice served during the last "
                     "90 days of the ONE-YEAR period tolls it for 90 days (about 1 year + 90 days total). "
                     "A notice served earlier does not extend the deadline. CCP 364 also bars filing suit "
                     "until 90 days after the notice is served. Whether/how 364(d) affects the 3-year "
                     "outside limit is a question for counsel."),
        },
        "notes": [],
    }
    if governing.startswith("3-year"):
        res["notes"].append("The 3-year outside limit governs here. The 364(d) extension shown is uncertain "
                            "for the 3-year period; ask an attorney.")
    if notice:
        if win_start <= notice <= earliest:
            res["ccp_364"]["notice_result"] = (f"Notice {notice} is inside the window: estimated extended "
                                               f"deadline {earliest + dt.timedelta(days=90)}.")
        elif notice < win_start:
            res["ccp_364"]["notice_result"] = (f"Notice {notice} is BEFORE the window: no extension; "
                                               f"deadline stays {earliest}. Suit may not be filed until "
                                               f"{notice + dt.timedelta(days=90)} or later.")
        else:
            res["ccp_364"]["notice_result"] = f"Notice {notice} is AFTER the estimated deadline {earliest}."
    if public_entity:
        res["government_claims_act"] = {
            "claim_due_6_months_from_injury": add_months(injury, 6),
            "claim_due_6_months_from_discovery": add_months(discovery, 6),
            "late_claim_application_by_1_year_from_injury": add_years(injury, 1),
            "late_claim_application_by_1_year_from_discovery": add_years(discovery, 1),
            "note": ("Public entities (e.g., county/district/UC hospitals and their employees): a written "
                     "claim generally must be presented within 6 months after accrual (Gov. Code 911.2). "
                     "If missed, a late-claim application must be made within a reasonable time not to "
                     "exceed 1 year after accrual (Gov. Code 911.4). After written rejection, suit is "
                     "generally due within 6 months of the notice; if no proper notice, 2 years from "
                     "accrual (Gov. Code 945.6). Accrual uses the same discovery concepts; the "
                     "injury-based dates are the conservative ones. Federal facilities (VA, FQHCs) follow "
                     "the FTCA instead."),
        }
    for d in {one_year, three_year, earliest}:
        w = weekend_note(d)
        if w:
            res["notes"].append(w)
    if today:
        res["days_remaining_to_earliest"] = (earliest - today).days
        if res["days_remaining_to_earliest"] < 0:
            res["notes"].append("The estimated earliest deadline has PASSED. Exceptions (fraud, intentional "
                                "concealment, foreign body, estoppel, minority) may or may not apply. See an "
                                "attorney immediately.")
    return res


def fmt(res):
    c, n = res["ccp_340_5"], res["ccp_364"]
    out = [BANNER, "",
           f"Injury date:              {res['inputs']['injury']}",
           f"Discovery/suspicion date: {res['inputs']['discovery']}", "",
           "CCP 340.5",
           f"  1 year after discovery:   {c['one_year_from_discovery']}",
           f"  3 years after injury:     {c['three_years_from_injury']}",
           f"  EARLIEST (estimated):     {c['earliest_deadline']}   <- governing: {c['governing_period']}"]
    if "days_remaining_to_earliest" in res:
        out.append(f"  Days remaining:           {res['days_remaining_to_earliest']}")
    out += ["", "CCP 364 (90-day notice of intent to sue)",
            f"  Notice window:            {n['notice_window_start']} to {n['notice_window_end']}",
            f"  Extended deadline if notice served in window: {n['extended_deadline_if_served_in_window']}",
            f"  {n['note']}"]
    if "notice_result" in n:
        out.append(f"  -> {n['notice_result']}")
    g = res.get("government_claims_act")
    if g:
        out += ["", "Government Claims Act (public entities)",
                f"  6-month claim (from injury / discovery):        {g['claim_due_6_months_from_injury']} / {g['claim_due_6_months_from_discovery']}",
                f"  Late-claim application, 1 yr (injury / discovery): {g['late_claim_application_by_1_year_from_injury']} / {g['late_claim_application_by_1_year_from_discovery']}",
                f"  {g['note']}"]
    if res["notes"]:
        out += ["", "Notes"] + [f"  * {x}" for x in res["notes"]]
    out += ["", "3-year limit tolling exceptions in CCP 340.5: (1) fraud, (2) intentional concealment,",
            "(3) a non-therapeutic foreign body. The 1-year period has no such tolling (Sanchez v. South",
            "Hoover Hospital). Equitable estoppel may bar a defendant who induced delay (Doe v. Marten).",
            "See deadlines/README.md.", "", BANNER]
    return "\n".join(out)


def main(argv=None):
    p = argparse.ArgumentParser(description="CA med-mal deadline estimator. NOT LEGAL ADVICE.")
    p.add_argument("--injury", required=True)
    p.add_argument("--discovery", required=True)
    p.add_argument("--notice")
    p.add_argument("--public-entity", action="store_true")
    p.add_argument("--today")
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    res = compute(parse(a.injury, "injury"), parse(a.discovery, "discovery"),
                  parse(a.notice, "notice") if a.notice else None, a.public_entity,
                  parse(a.today, "today") if a.today else dt.date.today())
    if a.json:
        print(json.dumps(res, default=str, indent=2))
    else:
        print(fmt(res))


if __name__ == "__main__":
    main()
