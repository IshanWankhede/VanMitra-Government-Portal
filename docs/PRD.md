# Product Requirements: VanMitra Government Portal

## Problem
Community Forest Rights (CFR) claims under the Forest Rights Act move from Gram Sabha through the Sub-Divisional Level Committee (SDLC) to the District Level Committee (DLC). Officers need one place to examine claims, record decisions with remarks, collect the required signatures and keep an auditable history. The villager-facing Flutter app creates the claims; this portal is the government counterpart.

## Users
| Role | Purpose |
|---|---|
| SDO (SDLC) | Examines submitted claims; forwards to DLC or sends back |
| DFO / DCF | DLC member; reviews and signs the title |
| District Tribal Welfare Officer | DLC member; reviews and signs |
| District Collector / Deputy Commissioner | DLC chair; reviews and signs |
| Government Admin (records office) | Updates records, activates CFR, monitors all claims |

## Goals
Secure login; role-specific dashboards; claim review with documents, evidence, map and verification data; remand with remarks; forwarding; three-officer approval with signatures; title document generation; notifications; complete audit trail.

## Non-goals
Replacing the statutory process; deciding legal eligibility; official cadastral survey; real digital signatures (mock only until an approved mechanism is confirmed); real-time infrastructure.

## Key rules
- Each role sees only its own work: **Needs my action** and **Handled by me**. Admin sees all. Out-of-scope claims return 404.
- Gram Sabha stages never appear in the portal.
- UI requests actions; the backend validates and records the transition. Every action creates a workflow event and audit record; history is never overwritten.
- Maps are "Community Map / Submitted Mapping Data", never an official survey. Completeness meter means documentation completeness, not approval odds.

## Functional requirements
FR1 Auth and sessions. FR2 Role-scoped dashboard. FR3 Claims list (scope tabs, search, filters, pagination). FR4 Claim workspace: overview, documents, evidence, map, verification, workflow, review, title, audit. FR5 SDO examination checklist before forwarding. FR6 Remand with required remarks. FR7 Approve and sign by DFO, DTWO, Collector; title issued after the third signature. FR8 Title document generation (versioned). FR9 Notifications with unread count. FR10 Audit log, read-only.

## Non-functional requirements
Desktop-first, responsive to tablet; WCAG AA contrast, keyboard use, visible focus; loading/empty/error states; light and dark themes; no secrets in the browser; indexed queries; documented API.

## Acceptance (summary)
Each demo role logs in and sees a different, non-empty inbox. SDO examines and forwards; three DLC officers sign; title is generated with three signatures; admin completes the record; Collector never sees a claim before the SDO forwards it; audit shows every step. See `PHASES.md` and the phase prompts for per-phase checks.

Assumptions and open questions: `ASSUMPTIONS.md`.
