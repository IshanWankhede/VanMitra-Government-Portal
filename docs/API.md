# API contract

Base URL `http://localhost:8000/api`. Swagger at `/docs`. Auth: `Authorization: Bearer <token>`.
Success `{success:true,data,message}`; lists add `pagination:{page,limit,total,totalPages}`; error `{success:false,error:{code,message}}`.
Statuses: 401 not logged in/expired, 403 role not allowed, 404 not found or not visible to you, 409 invalid state transition, 422 validation.

## Built
| Method | URL | Notes |
|---|---|---|
| POST | /auth/login | `{email,password}` returns `{token,user}` |
| GET | /auth/me | current user |
| POST | /auth/logout | stateless; client discards token |
| GET | /government/dashboard | role-scoped: `inboxCount, handledCount, byStatus, inbox[], recentHandled[]` |
| GET | /government/claims | `scope=inbox\|handled\|all` (all = admin), `page, page_size, search, status, district, subdivision, village, from_date, to_date` |
| GET | /government/claims/{id} | includes `allowedActions` for your role; 404 if not visible |
| GET | /government/claims/{id}/timeline | workflow events |
| GET | /government/claims/{id}/audit | audit records |
| POST | /government/claims/{id}/actions | `{action, remarks?}`; actions per `WORKFLOW.md` |

## Planned
Documents (`/claims/{id}/documents`, `/documents/{id}`, verify/mark issue/request correction), evidence, reviews (`POST /claims/{id}/review`), examination checklist on FORWARD, title (`GET /claims/{id}/title`, `POST .../title/generate`, `POST .../title/sign` with a signature image, `GET .../title/signatures`, `GET .../title/final`), notifications (`GET /notifications`, `PATCH /notifications/{id}/read`), health (`GET /health`). Versioning (`/api/v1`) is recommended before the real backend integration.

## Example
```http
POST /api/government/claims/CFR-2026-0002/actions
{"action":"REMAND","remarks":"Boundary description is incomplete."}
```
