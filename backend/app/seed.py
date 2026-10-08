"""Development seed. Usage: python -m app.seed [--reset]
--reset clears collections ONLY if the configured database name ends with _dev."""
import asyncio, sys
from datetime import datetime, timedelta, timezone
from . import database
from .config import settings
from .database import db
from .security import hash_pw

USERS = [("admin@dev.local", "Dev Admin", "GOVERNMENT_ADMIN"), ("sdo@dev.local", "Dev SDO", "SDO_OFFICER"),
         ("dfo@dev.local", "Dev DFO", "DFO_DCF"), ("dtwo@dev.local", "Dev DTWO", "DISTRICT_TRIBAL_WELFARE_OFFICER"),
         ("collector@dev.local", "Dev Collector", "DISTRICT_COLLECTOR")]
EMAIL = {r: e for e, _, r in USERS}; NAME = {r: n for _, n, r in USERS}
PLACES = [("Kurkheda", "Gadchiroli", "Kurkheda"), ("Dhanora", "Gadchiroli", "Dhanora"), ("Aheri", "Gadchiroli", "Aheri"),
          ("Korchi", "Gadchiroli", "Korchi"), ("Armori", "Gadchiroli", "Armori"), ("Chamorshi", "Gadchiroli", "Chamorshi"),
          ("Salekasa", "Gondia", "Deori"), ("Chichgarh", "Gondia", "Deori"), ("Navegaon", "Gondia", "Deori")]
# (status, how many). No pre-submission (Gram Sabha) states: those live in the community app.
PLAN = [("SUBMITTED_SDLC", 4), ("SDLC_UNDER_EXAM", 3), ("REMANDED_TO_GS", 3), ("SDLC_FORWARDED", 4),
        ("DLC_UNDER_CONSIDERATION", 3), ("TITLE_APPROVED", 3), ("RECORD_UPDATED", 2), ("CFR_ACTIVE", 2)]
PATH = ["SUBMITTED_SDLC", "SDLC_UNDER_EXAM", "SDLC_FORWARDED", "DLC_UNDER_CONSIDERATION", "TITLE_APPROVED", "RECORD_UPDATED", "CFR_ACTIVE"]
PEND = {"SUBMITTED_SDLC": "SDO (SDLC)", "SDLC_UNDER_EXAM": "SDO (SDLC)", "REMANDED_TO_GS": "Gram Sabha", "SDLC_FORWARDED": "DLC",
        "DLC_UNDER_CONSIDERATION": "DLC", "TITLE_APPROVED": "Records office", "RECORD_UPDATED": "Records office", "CFR_ACTIVE": "None"}
ACTOR = {"SDLC_UNDER_EXAM": "SDO_OFFICER", "SDLC_FORWARDED": "SDO_OFFICER", "REMANDED_TO_GS": "SDO_OFFICER",
         "DLC_UNDER_CONSIDERATION": "DFO_DCF", "TITLE_APPROVED": "DISTRICT_COLLECTOR",
         "RECORD_UPDATED": "GOVERNMENT_ADMIN", "CFR_ACTIVE": "GOVERNMENT_ADMIN"}

def event(cid, prev, s, ts, role=None, remarks="Mock historical event"):
    r = role or ACTOR.get(s)
    return {"claimId": cid, "actorId": EMAIL.get(r, "system"), "actorName": NAME.get(r, "Seed"), "actorRole": r or "SYSTEM",
            "action": "SEED_STATE", "fromStatus": prev, "toStatus": s, "remarks": remarks, "timestamp": ts}

async def main():
    if settings.mongodb_database.endswith("_dev") is False and "--reset" in sys.argv:
        sys.exit("Refusing to reset: database name must end with _dev")
    await database.connect(); d = db()
    if "--reset" in sys.argv:
        for c in ("users", "claims", "workflowEvents", "auditLogs"): await d[c].delete_many({})
    for e, n, r in USERS:
        await d.users.update_one({"email": e}, {"$set": {"email": e, "name": n, "role": r, "isDevAccount": True, "passwordHash": hash_pw("Dev@12345")}}, upsert=True)
    t0, i = datetime.now(timezone.utc) - timedelta(days=60), 0
    for status, n in PLAN:
        for _ in range(n):
            i += 1; cid = f"CFR-2026-{i:04d}"
            if await d.claims.find_one({"claimId": cid}): continue
            v, dist, sub = PLACES[i % len(PLACES)]
            created = (t0 + timedelta(days=i * 2)).isoformat()
            await d.claims.insert_one({"claimId": cid, "claimant": f"{v} Gram Sabha community", "village": v, "gramSabha": f"{v} Gram Sabha",
                "district": dist, "subdivision": sub, "claimType": "CFR", "areaHa": round(300 + (i * 97) % 1500, 1), "status": status,
                "pendingWith": PEND[status], "createdAt": created, "updatedAt": created, "isMockData": True})
            stages = ["SUBMITTED_SDLC", "SDLC_UNDER_EXAM", "REMANDED_TO_GS"] if status == "REMANDED_TO_GS" else PATH[:PATH.index(status) + 1]
            prev, base = None, datetime.fromisoformat(created)
            for k, s in enumerate(stages):
                ts = (base + timedelta(days=k)).isoformat()
                evs = [event(cid, prev, s, ts, "SYSTEM" if k == 0 else None, "Claim submitted" if k == 0 else "Mock historical event")]
                if s == "DLC_UNDER_CONSIDERATION":  # other DLC members reviewed too
                    evs.append(event(cid, s, s, ts, "DISTRICT_TRIBAL_WELFARE_OFFICER"))
                for ev in evs:
                    await d.workflowEvents.insert_one(dict(ev)); await d.auditLogs.insert_one(dict(ev))
                prev = s
            await d.claims.update_one({"claimId": cid}, {"$set": {"updatedAt": ts}})
    print("Seed complete. Dev password for all demo users: Dev@12345")
    await database.close()

asyncio.run(main())
