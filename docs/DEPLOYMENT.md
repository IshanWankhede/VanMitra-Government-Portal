# Running the project

## Docker (recommended)
```bash
cp .env.example .env      # fill MONGODB_URI, JWT_SECRET (see ATLAS_SETUP.md)
docker compose up --build            # UI http://localhost:5173, API http://localhost:8000, docs http://localhost:8000/docs
docker compose run --rm backend python -m app.seed             # seed
docker compose run --rm backend python -m app.seed --reset     # wipe dev collections, reseed (refuses if DB name does not end with _dev)
docker compose down                  # stop
docker compose up --build            # rebuild
```
MongoDB is NOT a container: it is Atlas.

## Without Docker
Backend: `cd backend && python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`, export the variables from `.env`, `python -m app.seed`, `uvicorn app.main:app --reload`.
Frontend: `cd frontend && npm install && npm run dev` (needs `VITE_API_BASE_URL`).

## Environment
`MONGODB_URI`, `MONGODB_DATABASE`, `JWT_SECRET`, `CORS_ORIGINS` (backend only). `VITE_API_BASE_URL` (browser-visible, no secrets).

## Switching to the real API
Change `VITE_API_BASE_URL` to the real base URL. Nothing else in the frontend changes if the contract in `API.md` is respected.

## Production notes
Use a production frontend build behind nginx or a static host, HTTPS, a strong rotating `JWT_SECRET`, restricted CORS origins, Atlas IP allow-list for the server, httpOnly cookies instead of localStorage tokens, and a real document store. No secrets in images or git.
