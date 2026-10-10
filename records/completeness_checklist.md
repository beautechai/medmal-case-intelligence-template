# Records completeness checklist

Work through this for **each facility and each encounter**. Record findings in `inventory.csv` (`notes`) and follow-up requests in `../evidence/record_requests.csv`. Checkboxes are for your private copy.

## 1. Page and Bates continuity
- [ ] Every production has a Bates/page range; ranges recorded in the inventory.
- [ ] No skipped numbers (e.g., 0300 to 0316). List every gap and ask the custodian in writing to explain or produce.
- [ ] Page counts in the file match the custodian's certification/declaration.
- [ ] No duplicate Bates numbers with different content.
- [ ] Multi-page notes are complete (look for "page 2 of 3" with page 3 missing, truncated lines, cut-off signatures).
- [ ] Scanned pages are legible; request native/electronic copies of illegible pages.

## 2. Encounter coverage
- [ ] List every encounter you know of (ED visits, admissions, clinic visits, transfers, telehealth, home health, rehab). Use bills, EOBs, portal visit lists and your own calendar to build the list.
- [ ] Each encounter has: registration/face sheet, H&P or ED provider note, progress notes for every day, orders, results, discharge summary or transfer note.
- [ ] Every calendar day of each inpatient stay has physician progress notes **and** nursing documentation.
- [ ] Transfer paperwork exists at both the sending and receiving facility (transfer form, physician certification, accepting physician, report given).
- [ ] Outside records referenced in the chart ("see outside labs/imaging") were also obtained.

## 3. Portal vs. production cross-check
- [ ] Compare portal downloads with the certified production note by note: dates, times, authors, content, signatures.
- [ ] Flag any note that exists in one but not the other, or whose wording, timestamps or author differ. Differences can indicate later edits; the audit trail (section 6) is how to confirm.
- [ ] Compare lab results in the portal vs. production (values, collection times, reference ranges).
- [ ] Compare imaging report text and finalization times.
- [ ] Save dated copies of portal pages now; portal content can change or disappear.

## 4. Commonly missing sections (request explicitly by name)
- [ ] **Code blue / rapid-response team** records: event flowsheet, times, medications given, attendees, debrief notes.
- [ ] **Anesthesia record for every surgical case**: pre-anesthesia evaluation, intraoperative record (vitals, meds, fluids, EBL), post-anesthesia (PACU) notes.
- [ ] **Operative/procedure notes for every procedure**, plus brief op notes, implant logs, counts (sponge/needle/instrument), pathology.
- [ ] **Nursing notes and flowsheets**: vitals, I&O, pain scores, wound assessments, neuro checks, fall/skin risk, shift assessments.
- [ ] **Medication Administration Record (MAR)** including held/refused doses and override (e.g., automated dispensing cabinet) reports.
- [ ] **Physician and nursing orders**, including verbal/telephone orders and their co-signatures.
- [ ] **Consent forms** for every procedure, blood products and anesthesia.
- [ ] **Wound care documentation**: photos, measurements, wound VAC settings and changes.
- [ ] **Imaging**: reports *and* the actual images (DICOM) on disc or via a link.
- [ ] **Pathology and microbiology** (cultures and sensitivities).
- [ ] **Telemetry/monitor strips and alarm logs**, if relevant.
- [ ] **Consult notes** (ID, wound care, surgery, nephrology, etc.).
- [ ] **Discharge instructions and medication reconciliation**.
- [ ] **Billing records / itemized bill**: they show services charged that may be missing from the chart.
- [ ] **Patient communications**: portal messages, call logs, after-hours nurse line notes.
- [ ] **Audit trail / access log** for the encounter (see `audit_trail_request_guide.md`).

## 5. Signature and timing review
- [ ] Every note signed; record unsigned/pended notes.
- [ ] Compare **date of service vs. signing/filing time** for op notes, discharge summaries and key progress notes (enter in `../procedures/`).
- [ ] Late entries and **addenda** are labeled as such, with their own timestamps.
- [ ] Co-signatures for trainee notes and verbal orders.

## 6. Follow-up
- [ ] For every gap above, add a row to `../evidence/record_requests.csv` with a due date.
- [ ] Ask for a custodian-of-records **declaration/certification** stating the production is complete.
- [ ] Share the gap list with your attorney.
