# Roles and visibility

Backend authorization is final. Hiding a button in React is never security.

| Role code | Title | Actions |
|---|---|---|
| SDO_OFFICER | Sub-Divisional Officer (SDLC) | Start examination, forward, send back |
| DFO_DCF | Divisional Forest Officer / DCF | Start consideration, approve and sign, send back |
| DISTRICT_TRIBAL_WELFARE_OFFICER | District Tribal Welfare Officer | same as DFO_DCF |
| DISTRICT_COLLECTOR | District Collector / Deputy Commissioner | same as DFO_DCF |
| GOVERNMENT_ADMIN | Government admin (records office) | Update record, activate CFR; view all |

Planned permissions: VIEW_CLAIMS, VIEW_DOCUMENTS, REVIEW_CLAIMS, ADD_REMARKS, REMAND_CLAIMS, FORWARD_CLAIMS, APPROVE_CLAIMS, GENERATE_TITLE, SIGN_TITLE, VIEW_AUDIT, MANAGE_USERS.

## Who sees which claim
| Claim state | SDO | DFO / DTWO / Collector | Admin |
|---|---|---|---|
| SUBMITTED_SDLC, SDLC_UNDER_EXAM | Inbox | not visible | visible |
| REMANDED_TO_GS | Handled ("Sent back") | Handled only if they sent it back | visible |
| SDLC_FORWARDED, DLC_UNDER_CONSIDERATION | Handled | Inbox until they act, then Handled | visible |
| TITLE_APPROVED, RECORD_UPDATED | Handled | Handled | Inbox |
| CFR_ACTIVE | Handled | Handled | visible |

Implementation (`visibility.py`): **inbox** = claims whose state has an action allowed for the role; **handled** = claims with a workflow event by that user; **all** = admin only (403 otherwise). A claim outside a role's visible set returns **404**, so existence is not leaked. Jurisdiction filtering (district/subdivision) is planned, not yet enforced.
