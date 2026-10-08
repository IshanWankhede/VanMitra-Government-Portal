# Security
- No secrets in React, `VITE_*`, Dockerfiles or git. `.env` is ignored; `.env.example` holds placeholders. `MONGODB_URI` exists only on the backend.
- Passwords hashed with bcrypt. JWT with expiry (`jwt_expire_minutes`). Logout is client-side for now; server-side revocation is a production task.
- Backend RBAC on every action; visibility enforced in `visibility.py`; out-of-scope claims return 404.
- CORS from env, never `*` in production.
- Audit and workflow events are append-only (no edit/delete endpoint).
- Demo accounts are marked `isDevAccount` and must not exist in production.
- Known dev trade-offs: token in `localStorage` (use httpOnly cookies in production); no rate limiting yet; jurisdiction filtering not yet enforced; document access control arrives with the documents module.
- Seed `--reset` refuses to run unless the database name ends with `_dev`.
- Signatures are MOCK only and carry a visible "Development / Mock Signature" label until an approved eSign/DSC mechanism is confirmed.
