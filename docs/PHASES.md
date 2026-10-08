# Build phases and where you are now

## Your approach (prototype first)
1. Design the whole frontend in Google AI Studio (mock data, no backend). Copy that code into `prototype/` (git-ignored).
2. Build the real backend (FastAPI + MongoDB Atlas) from the API contract.
3. Copy the prototype's UI into `frontend/`, replace its mock API with real API calls. The UI stays, only the data source changes.

## Status
| Phase | Name | Status |
|---|---|---|
| 0 | Prototype in Google AI Studio (`prototype/`) | IN PROGRESS (you) |
| 1 | Documentation and API contract (`docs/`) | DONE in this repo; the agent verifies it against the prototype's `mockApi` |
| 2 | Backend core: auth, roles, claims, visibility, seed | STARTER DONE (see below), needs completion |
| 3 | Docker and Atlas hardening | Starter files exist, needs verification |
| 4 | Frontend import from prototype | NOT STARTED (needs finished prototype) |
| 5 | Wire dashboard + claims | Starter UI exists; replaced by prototype in phase 4 |
| 6 | Wire claim workspace (documents, evidence, map, verification) | NOT STARTED |
| 7 | Review, remand, forward, examination checklist | Backend actions done; UI and checklist pending |
| 8 | Title, 3 signatures, PDF | NOT STARTED |
| 9 | Notifications | NOT STARTED |
| 10 | Tests | NOT STARTED |
| 11 | Integration readiness and final | NOT STARTED |

**You are here: Phase 0, about to start Phase 2/3.** Do not wait for the prototype to finish to start the backend: the backend needs only `docs/API.md`, `DATABASE.md` and `WORKFLOW.md`.

## What the starter code already does
Login (JWT), 5 roles, role-scoped inbox/handled lists, claim detail, timeline, audit, workflow actions with backend validation, seed data (24 claims), Docker files, a basic React shell. It is a foundation, not the finished product.

## Recommended order from here
1. Create your Atlas database (`ATLAS_SETUP.md`), run the backend, seed, open `/docs`.
2. Give your coding agent `prompts/00_SHARED_CONTEXT.md` + `prompts/02_PHASE_BACKEND_COMPLETE.md`.
3. Finish the prototype in AI Studio; copy it into `prototype/`.
4. Run phase 4 onward (frontend import and wiring).

Each phase file is in `prompts/` and ends with a commit message.
