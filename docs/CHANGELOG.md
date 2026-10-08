# Changelog
## Unreleased
- Restructured around a prototype-first workflow (`prototype/`, git-ignored).
- Roles corrected: SDO, DFO/DCF, DTWO, Collector, Admin (removed SDLC_OFFICER, DLC_OFFICER).
- Role-scoped visibility: inbox / handled / all; out-of-scope claims return 404.
- Role-specific dashboard KPIs; Claims page scope tabs.
- Seed: 24 claims, no Gram Sabha stages, demo actors per role; `--reset` guarded to `_dev` databases.
- Full documentation set and updated phase prompts.
## 0.1.0 Starter
- FastAPI + Atlas connection, JWT auth, workflow actions, claims list/detail, React shell, Docker files.
