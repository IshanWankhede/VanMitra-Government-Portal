# MongoDB Atlas setup, step by step (development database)

Atlas screens change occasionally; names below may differ slightly.

1. Go to https://www.mongodb.com/cloud/atlas and sign up or log in.
2. Create a **Project**: name it `VanMitra Government Portal`.
3. Click **Create** (or **Build a Database**) and pick the **Free (M0)** tier.
4. Provider/region: choose a nearby region (for example AWS, Mumbai `ap-south-1`).
5. Cluster name: `vanmitra-gov-dev`. Click **Create**.
6. **Database user:** Security > Database Access > Add New Database User. Choose password authentication, a username like `vanmitra_dev`, and a strong password (use Atlas "Autogenerate"). Role: *Read and write to any database* (fine for dev). Save the password somewhere safe.
7. **Network access:** Security > Network Access > Add IP Address > **Add Current IP Address**. Do not use `0.0.0.0/0` permanently. If your IP changes (new Wi-Fi), add the new one. If you use Docker on the same machine the same IP works.
8. **Connection string:** Database > your cluster > **Connect** > **Drivers** > Python. Copy the string. It looks like `mongodb+srv://vanmitra_dev:<password>@vanmitra-gov-dev.xxxxx.mongodb.net/?retryWrites=true&w=majority`.
9. Replace `<password>` with your password. If it has special characters (`@ : / ? # %`), URL-encode them (for example `@` becomes `%40`).
10. Copy `.env.example` to `.env` in the repo root and set:
    ```
    MONGODB_URI=<your string>
    MONGODB_DATABASE=vanmitra_government_dev
    JWT_SECRET=<long random string>
    ```
    Generate a secret with `python -c "import secrets;print(secrets.token_urlsafe(48))"`. Never commit `.env`.
11. Start the backend (`docker compose up --build`), then seed: `docker compose run --rm backend python -m app.seed`.
12. Check the data: Atlas > Database > **Browse Collections** > `vanmitra_government_dev`. You should see `users`, `claims`, `workflowEvents`, `auditLogs`. The database appears only after the first write (the seed).
13. Open http://localhost:8000/docs and try `POST /api/auth/login` with `sdo@dev.local` / `Dev@12345`.

## Troubleshooting
| Symptom | Fix |
|---|---|
| Timeout / "server selection error" | Your IP is not on the allow list (step 7); VPN or new network |
| "bad auth" / authentication failed | Wrong username/password; password not URL-encoded |
| DNS / SRV error | Network blocks SRV lookups; try another network or the non-SRV string from Atlas |
| Backend exits at startup | `.env` missing `MONGODB_URI` or `JWT_SECRET` |
| No collections shown | You have not run the seed yet |

Later, to point at the shared production database, only the backend `MONGODB_URI` and `MONGODB_DATABASE` change.
