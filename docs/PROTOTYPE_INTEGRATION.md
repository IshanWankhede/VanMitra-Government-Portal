# Using the AI Studio prototype

## Idea
`prototype/` holds the code exported from Google AI Studio. It is a visual and behavioural reference with its own mock API. It is **git-ignored** (see `.gitignore`), so it stays on your machine.

## Steps
1. In AI Studio, export or copy the full project. Put it in `prototype/` and run it on its own (`npm install`, `npm run dev`) to confirm it works.
2. Keep the prototype's `services/mockApi.js` as the **reference for response shapes** and workflow rules. Use it to check `docs/API.md` (the agent compares them in Phase 1).
3. **Phase 4:** copy `prototype/src/{components,layouts,pages,styles,constants,i18n}` into `frontend/src` (replace the starter pages). Keep from the starter: `services/api/client.js`, `context/Auth.jsx`, `Dockerfile`, `vite.config.js`.
4. Replace every import of `mockApi` with the real service files in `frontend/src/services/api/` that call the backend. Keep the same function names where possible (for example `claimsApi.list({scope})`) so pages do not change.
5. Remove prototype-only things: the persona switcher (real login replaces it; keep quick demo-login chips only when `VITE_DEMO_MODE=true`), any "simulate error" toggle, and hard-coded users.
6. Wire page by page (phases 5 to 9). After each, compare with the prototype side by side.

## Mapping (mock to real)
| Prototype call | Backend endpoint |
|---|---|
| login / current user | POST /auth/login, GET /auth/me |
| dashboard | GET /government/dashboard |
| claims list | GET /government/claims?scope= |
| claim detail | GET /government/claims/{id} |
| timeline / audit | GET /government/claims/{id}/timeline, /audit |
| workflow action | POST /government/claims/{id}/actions |
| sign / title | planned: POST /title/sign, GET /title |
| notifications | planned: GET /notifications |

## Rules
Visibility and permissions come from the backend; the UI must not filter other roles' claims itself. If the prototype and `API.md` disagree, update `API.md` and the backend deliberately, and note it in `CHANGELOG.md`.
