# CSV headers

Header line for each table. Column descriptions, required fields and allowed values live in the matching `*.schema.json` file. Copy a header into a new CSV or start from the `*_TEMPLATE.csv` file.

## records_inventory

Template: `records/inventory_TEMPLATE.csv` · Required: `doc_id`, `facility`, `source_type`

```
doc_id,facility,source_type,request_id,doc_type,encounter_id,date_of_service_start,date_of_service_end,bates_start,bates_end,page_count,file_name,received_date,certified,notes
```

## labs

Template: `labs/labs_TEMPLATE.csv` · Required: `facility`, `collected_date`, `analyte`

```
facility,encounter_id,collected_date,collected_time,analyte,value,unit,ref_low,ref_high,flag,specimen,source_doc_id,page,notes
```

## lab_events

Template: `labs/lab_events_TEMPLATE.csv` · Required: `date`, `label`

```
date,label,category
```

## medications

Template: `medications/medications_TEMPLATE.csv` · Required: `med_id`, `medication`, `action`, `action_date`

```
med_id,medication,dose,route,frequency,action,action_date,action_time,actor_role,ordering_role,reason,facility,encounter_id,source_doc_id,page,notes
```

## procedures

Template: `procedures/procedures_TEMPLATE.csv` · Required: `proc_id`, `date_of_service`, `procedure`, `category`

```
proc_id,date_of_service,start_time,end_time,procedure,category,site,extent,performed_by_role,consent_signed_datetime,consent_doc_id,note_signed_datetime,note_filed_datetime,filing_lag_hours,facility,encounter_id,source_doc_id,page,notes
```

## events

Template: `events/events_TEMPLATE.csv` · Required: `event_id`, `date`, `category`, `description`

```
event_id,date,time,location,channel,person_role,stated_role,actual_role_verified,role_misidentified,category,description,witnesses,contemporaneous_note,evidence_doc_id,reported_to,reported_date,notes
```

## social_media_review

Template: `social-media/social_media_review_TEMPLATE.csv` · Required: `post_id`, `platform`

```
post_id,platform,post_date,locator,content_summary,mentions_provider,mentions_injury_or_activity,risk_rank,risk_reason,preserved,preservation_method,preserved_date,shown_to_counsel,notes
```

## evidence_index

Template: `evidence/evidence_index_TEMPLATE.csv` · Required: `doc_id`, `title`

```
doc_id,title,doc_type,author_role,facility,date,bates_start,bates_end,private_location,sha256,relevance,linked_ids,notes
```

## record_requests

Template: `evidence/record_requests_TEMPLATE.csv` · Required: `request_id`, `facility`

```
request_id,facility,department,records_requested,legal_basis,method,requested_date,sent_date,due_date,followup_date,received_date,pages_received,certified,certification_date,gaps_identified,status,notes
```
