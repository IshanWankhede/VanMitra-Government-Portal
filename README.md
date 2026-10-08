# VanMitra Government Portal

Government web portal for reviewing, forwarding, remanding and approving Forest Rights Act (FRA) Community Forest Rights claims. React (JavaScript, Vite) + FastAPI + MongoDB Atlas, Dockerized.

**Start here:** `docs/README.md` (index) and `docs/PHASES.md` (roadmap and where you are).

## Quick start
1. Create the Atlas database: `docs/ATLAS_SETUP.md`.
2. `cp .env.example .env` and fill `MONGODB_URI`, `JWT_SECRET`.
3. `docker compose up --build`  (UI :5173, API :8000, Swagger :8000/docs).
4. `docker compose run --rm backend python -m app.seed`
5. Log in at http://localhost:5173 (password `Dev@12345`): `sdo@dev.local`, `dfo@dev.local`, `dtwo@dev.local`, `collector@dev.local`, `admin@dev.local`.

Each role sees only its own claims (Needs my action / Handled). See `docs/RBAC.md`.

## Repo map
`backend/` FastAPI starter · `frontend/` React starter (replaced by the prototype UI in Phase 4) · `prototype/` AI Studio code (git-ignored) · `prompts/` phase prompts for the coding agent · `docs/` all documentation.

More detail: `docs/DEPLOYMENT.md`, `docs/FOLDER_STRUCTURE.md`.
