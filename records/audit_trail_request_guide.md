# EHR audit trail and access log: request guide

Electronic health record (EHR) systems log who **created, viewed, edited, signed, printed or deleted** each item and **when**. The audit trail can show:

- when a note was actually written vs. the date of service it describes;
- whether notes were edited after an adverse event or after a complaint or records request;
- addenda and late entries, and who authored them;
- who accessed the chart (useful if you suspect improper access to your records).

> Not legal advice. Facilities sometimes resist producing audit trails outside litigation, and your attorney may prefer to obtain them by subpoena or discovery. Ask counsel before sending.

## Who to send it to
- The facility's **Health Information Management (HIM) / Medical Records** department, and
- the **Privacy Officer** (for access logs / "accounting of disclosures").

## What to request (adapt the list)

For each encounter (list encounter dates/IDs), please produce in **native electronic format (CSV/Excel) or searchable PDF**:

1. **Audit trail for every clinical document** (progress notes, op notes, anesthesia records, nursing notes, discharge summary, orders, MAR entries, results), showing for each action:
   - user name **and** role/credential;
   - action type (create, view, modify, sign, co-sign, addend, delete, print, export);
   - date and time with time zone, to the second;
   - workstation/device identifier, if available;
   - document/version identifier.
2. **All versions** of each note, including drafts, pended/unsigned versions and the text before and after each modification.
3. **All addenda and late entries**, with their creation and signing timestamps and the reason recorded.
4. **Order audit**: who entered, verified, modified, discontinued each order and when (including verbal/telephone orders and co-signatures).
5. **MAR audit**: scan/administration times, overrides, held/refused documentation.
6. **Access log** for the entire record for the period [start] to [present]: every user who viewed the chart.
7. **Accounting of disclosures** under HIPAA (45 CFR 164.528) for the same period.
8. A description of the audit fields and any **codes or abbreviations** used, and the name of the EHR system/version.

## Legal hooks to mention (verify with counsel)
- HIPAA right of access: **45 CFR 164.524** (designated record set; electronic copies in the form requested if readily producible).
- HIPAA accounting of disclosures: **45 CFR 164.528**.
- California patient access: **Health & Safety Code § 123100 et seq.** (including § 123110).
- Ask that the facility **preserve** all audit data and metadata for the encounters (a litigation-hold request; your attorney may send a formal preservation letter).

## Template letter (placeholders only)

```
[Date]
To: Health Information Management / Privacy Officer, [Facility]
Re: Request for EHR audit trail, document versions and access log
Patient: [Name]  DOB: [DOB]  MRN: [MRN]
Encounters: [dates / encounter numbers]

Under 45 CFR 164.524 and 164.528 and Cal. Health & Safety Code § 123100 et seq.,
I request the following in native electronic format:
  [items 1-8 above]
Please preserve all audit data and metadata for these encounters.
Please confirm receipt and the expected production date.
[Signature]
```

## Reviewing what you get
- Load it into a spreadsheet; sort by document, then timestamp.
- For each key note, record in `../procedures/` (or a notes column) the **date of service**, **first created**, **signed**, and **last modified** times.
- Flag edits after: the adverse event, your complaint, your records request, or a notice of intent to sue.
- Flag notes signed by someone who does not appear in the access log at the relevant time, or vice versa.
- Do not draw conclusions yourself; give the flagged list to your attorney and expert.
