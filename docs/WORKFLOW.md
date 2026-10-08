# Claim workflow (government side)

Gram Sabha work is done in the community app. A claim first appears for the SDO when it is submitted.

```mermaid
stateDiagram-v2
  [*] --> SUBMITTED_SDLC
  SUBMITTED_SDLC --> SDLC_UNDER_EXAM: SDO starts examination
  SDLC_UNDER_EXAM --> SDLC_FORWARDED: SDO forwards (checklist complete)
  SDLC_UNDER_EXAM --> REMANDED_TO_GS: SDO sends back (remarks)
  SDLC_FORWARDED --> DLC_UNDER_CONSIDERATION: DLC member starts
  DLC_UNDER_CONSIDERATION --> TITLE_APPROVED: all 3 sign
  DLC_UNDER_CONSIDERATION --> REMANDED_TO_GS: member sends back (remarks)
  TITLE_APPROVED --> RECORD_UPDATED: Admin
  RECORD_UPDATED --> CFR_ACTIVE: Admin
  REMANDED_TO_GS --> SUBMITTED_SDLC: Gram Sabha resubmits
```

| From | Action | To | Roles (assumption) |
|---|---|---|---|
| SUBMITTED_SDLC | START_EXAMINATION | SDLC_UNDER_EXAM | SDO |
| SDLC_UNDER_EXAM | FORWARD | SDLC_FORWARDED | SDO |
| SDLC_UNDER_EXAM | REMAND | REMANDED_TO_GS | SDO |
| SDLC_FORWARDED | START_CONSIDERATION | DLC_UNDER_CONSIDERATION | DFO, DTWO, Collector |
| DLC_UNDER_CONSIDERATION | APPROVE (placeholder, see below) | TITLE_APPROVED | DFO, DTWO, Collector |
| DLC_UNDER_CONSIDERATION | REMAND | REMANDED_TO_GS | DFO, DTWO, Collector |
| TITLE_APPROVED | RECORD_UPDATE | RECORD_UPDATED | Admin |
| RECORD_UPDATED | ACTIVATE | CFR_ACTIVE | Admin |

**Not yet built:** the three-signature rule. Target: each of DFO/DCF, DTWO and Collector signs once per round; the third signature moves the claim to TITLE_APPROVED and generates the title. A send-back voids that round's signatures (kept in audit, never deleted). Until Phase 8 the backend has a single-step APPROVE placeholder in `workflow.py`.

Other states in the project vocabulary (not used by the government portal): DRAFT, EVIDENCE_COLLECTION, MAPPING_IN_PROGRESS, FRC_VERIFICATION, GS_READY, GS_RESOLVED, MODIFIED_REJECTED, PETITION_FILED.

All role rules live in `backend/app/workflow.py` and are development assumptions to confirm (`ASSUMPTIONS.md`).
