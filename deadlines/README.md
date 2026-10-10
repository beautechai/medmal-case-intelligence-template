# deadlines/: California CCP § 340.5 calculator

> # ⚠️ NOT LEGAL ADVICE. CONSULT A LICENSED CALIFORNIA ATTORNEY NOW.
> **The calculator gives estimates only.** The key input, the date you *discovered or should have suspected* wrongdoing, is a legal question that courts often resolve **against** patients, and it can be **earlier than you think** (for example, the day you first said "something went wrong," complained, or asked for records because you suspected an error). Tolling, estoppel, minors, wrongful death, public and federal defendants, and day-counting rules can all change the result. **Treat the earliest date as your real deadline and get a lawyer well before it.** Statutes and case law change; verify everything with counsel.

## Run it

```bash
python3 deadlines/ca_340_5_calculator.py --injury 2030-03-01 --discovery 2030-05-15
python3 deadlines/ca_340_5_calculator.py --injury 2030-03-01 --discovery 2030-05-15 --notice 2031-03-01 --public-entity
python3 deadlines/ca_340_5_calculator.py --injury 2030-03-01 --discovery 2030-05-15 --json
```

(Dates above are fictional EXAMPLES.)

## What it computes

| Output | Rule |
|---|---|
| 1 year after discovery | CCP § 340.5: one year after the plaintiff discovers, or through reasonable diligence should have discovered, the injury |
| 3 years after injury | CCP § 340.5 outside limit: three years after the date of injury |
| **Earliest** | Whichever occurs first controls |
| CCP § 364 window | A 90-day notice of intent to sue is required before filing (§ 364(a)). If served during the last 90 days of the one-year period, the period is tolled 90 days (§ 364(d); *Woods v. Young*) |
| Government Claims Act | 6-month claim (Gov. Code § 911.2), late-claim application within 1 year (§ 911.4), suit within 6 months after written rejection or 2 years if no notice (§ 945.6) |

Leap-day and month-end edge cases are rounded to the **earlier** date. The calculator flags deadlines that land on weekends (see CCP §§ 12, 12a) but you should never plan to file on the last day.

## Key statutes

- **Code Civ. Proc. § 340.5**: "three years after the date of injury or one year after the plaintiff discovers, or through the use of reasonable diligence should have discovered, the injury, whichever occurs first." The 3-year limit is tolled only for **(1) fraud, (2) intentional concealment, or (3) the presence of a foreign body which has no therapeutic or diagnostic purpose or effect.** For minors there are separate rules (generally 3 years, or before the 8th birthday for minors under 6, whichever is longer); ask counsel.
- **Code Civ. Proc. § 364**: 90-day notice of intent to sue before filing a professional-negligence action against a health care provider.
- **Gov. Code §§ 911.2, 911.4, 945.6**: claims against California public entities and their employees.
- Federal facilities and federally deemed clinics (e.g., VA, many community health centers) fall under the **Federal Tort Claims Act**, which has its own administrative claim requirement (generally 2 years). Ask counsel.

## Key cases (citations verified online before inclusion)

Each citation was checked against published sources (Justia, Stanford SCOCAL, FindLaw/Casetext, appellate dockets) in 2026. Summaries are simplified; read the opinions.

| Case | Holding (simplified) |
|---|---|
| **Jolly v. Eli Lilly & Co. (1988) 44 Cal.3d 1103** | The limitations period begins when the plaintiff *suspects or should suspect* that the injury was caused by wrongdoing, i.e., that "someone has done something wrong" to them. The plaintiff need not know the specific facts; once suspicion exists, they "must go find the facts" and "cannot wait for the facts to find" them. |
| **Sanchez v. South Hoover Hospital (1976) 18 Cal.3d 93** | Applies the discovery rule to § 340.5; the one-year period runs from when the plaintiff is on inquiry notice. Cited for the rule that the **one-year period has no tolling provision**, not even for fraud or concealment (as applied in *Kleefeld*). |
| **Kleefeld v. Superior Court (1994) 25 Cal.App.4th 1680** | A spouse who suspected the provider's treatment caused a death (and complained to a licensing board) started the one-year clock then. Waiting for the board's investigation did **not** toll it, and a late § 364 notice did not save the claim. |
| **Doe v. Marten (2020) 49 Cal.App.5th 1022** | A physician was **equitably estopped** from asserting the one-year bar because his response to the patient's arbitration demand reasonably induced her not to file suit. Estoppel requires conduct that actually and reasonably induced the delay. |
| **Brown v. Bleiberg (1982) 32 Cal.3d 426** | Affirmative misrepresentations about the nature and necessity of a surgery can raise a triable issue of **intentional concealment** tolling the outside limit, even after many years. Explains the history and structure of § 340.5's two periods. |
| **Norgart v. Upjohn Co. (1999) 21 Cal.4th 383** | Restates the discovery rule: accrual is postponed until the plaintiff suspects, or has reason to suspect, a *factual basis* (not a legal theory) for the claim's elements. In a wrongful-death case, suspicion shortly after death started the clock. |
| **Woods v. Young (1991) 53 Cal.3d 315** | A § 364(a) notice served in the **last 90 days** of the one-year period **tolls** the period 90 days (about 1 year + 90 days to file). Notice served earlier does not extend the deadline. |

## Tolling and estoppel: what to ask your attorney

- **Fraud / intentional concealment / foreign body**: these can extend the **3-year** outside limit (§ 340.5; *Brown v. Bleiberg*). Intentional concealment generally requires affirmative misrepresentation, not mere silence. These do **not** extend the one-year discovery period.
- **Equitable estoppel**: if a defendant's words or conduct reasonably induced you to delay filing (e.g., promises to fix things, misleading statements about process), they may be estopped from relying on the deadline (*Doe v. Marten*). Document such statements in `events/`.
- **Records obstruction or altered records**: log every request, delay and discrepancy in `evidence/record_requests_*.csv` and `records/`; your attorney decides whether it matters legally.
- **Arbitration agreements**: check admission paperwork for arbitration clauses; they change the process.

## Sources

- CCP § 340.5: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=340.5
- CCP § 364: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=364
- Gov. Code § 911.2: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=GOV&sectionNum=911.2
- Gov. Code § 911.4: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=GOV&sectionNum=911.4
- Gov. Code § 945.6: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=GOV&sectionNum=945.6
- Kleefeld: https://law.justia.com/cases/california/court-of-appeal/4th/25/1680.html
- Doe v. Marten: https://law.justia.com/cases/california/court-of-appeal/2020/a153427.html
- Brown v. Bleiberg: https://law.justia.com/cases/california/supreme-court/3d/32/426.html
- Norgart v. Upjohn: https://law.justia.com/cases/california/supreme-court/4th/21/383.html
- Woods v. Young: https://law.justia.com/cases/california/supreme-court/3d/53/315.html
- Jolly v. Eli Lilly and Sanchez v. South Hoover Hospital are quoted and cited in Kleefeld and Norgart above.
