# Folder structure
```
vanmitra-gov-portal/
├── backend/
│   ├── app/
│   │   ├── main.py            app + CORS + error format + startup/shutdown
│   │   ├── config.py          env settings (MONGODB_URI, JWT_SECRET, CORS_ORIGINS)
│   │   ├── database.py        Mongo client (one per app) + indexes
│   │   ├── security.py        bcrypt, JWT, current_user
│   │   ├── workflow.py        state machine + role rules (edit rules here)
│   │   ├── visibility.py      who sees which claim (inbox/handled/all)
│   │   ├── seed.py            demo data (python -m app.seed)
│   │   └── routers/           auth.py, government.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/                  React + Vite (JavaScript)
│   └── src/ pages, components, context, constants, services/api, styles
├── prototype/                 AI Studio code (git-ignored, local only)
├── prompts/                   00 shared context + phase prompts 01..11 for the coding agent
├── docs/                      all documentation (see docs/README.md)
├── docker-compose.yml         frontend + backend (MongoDB is Atlas)
├── .env.example               placeholders only
└── README.md
```
Starter code you can ignore until needed: the planned folders (`schemas/`, `services/`, `repositories/`) appear when the coding agent reaches Phase 2.
