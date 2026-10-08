import re
from datetime import datetime, timezone
from typing import Optional
from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from ..database import db
from ..security import current_user, err
from ..visibility import can_see, scope_query
from ..workflow import REMARKS_REQUIRED, TRANSITIONS, allowed_actions

router = APIRouter(prefix="/government", tags=["government"])
now = lambda: datetime.now(timezone.utc).isoformat()
ok = lambda data, msg="OK", **x: {"success": True, "data": data, "message": msg, **x}

async def _claim(cid, user):
    c = await db().claims.find_one({"claimId": cid}, {"_id": 0})
    # 404 (not 403) for out-of-scope claims so their existence is not leaked
    if not c or not await can_see(user, cid):
        raise err(404, "CLAIM_NOT_FOUND", "Claim not found")
    return c

@router.get("/dashboard")
async def dashboard(user=Depends(current_user)):
    d = db(); admin = user["role"] == "GOVERNMENT_ADMIN"
    q_in, q_h = await scope_query(user, "inbox"), await scope_query(user, "handled")
    q_vis = {} if admin else await scope_query(user, "visible")
    by = {r["_id"]: r["n"] async for r in d.claims.aggregate([{"$match": q_vis}, {"$group": {"_id": "$status", "n": {"$sum": 1}}}])}
    return ok({"role": user["role"], "inboxCount": await d.claims.count_documents(q_in),
               "handledCount": await d.claims.count_documents(q_h), "byStatus": by,
               "inbox": await d.claims.find(q_in, {"_id": 0}).sort("updatedAt", -1).limit(5).to_list(5),
               "recentHandled": await d.claims.find(q_h, {"_id": 0}).sort("updatedAt", -1).limit(4).to_list(4)})

@router.get("/claims")
async def claims(user=Depends(current_user), scope: Optional[str] = None, page: int = 1, page_size: int = Query(20, le=100),
                 search: Optional[str] = None, status: Optional[str] = None, district: Optional[str] = None,
                 subdivision: Optional[str] = None, village: Optional[str] = None,
                 from_date: Optional[str] = None, to_date: Optional[str] = None):
    scope = scope or ("all" if user["role"] == "GOVERNMENT_ADMIN" else "inbox")
    if scope not in ("inbox", "handled", "all"):
        raise err(422, "BAD_SCOPE", "scope must be inbox, handled or all")
    conds = [await scope_query(user, scope)]
    for k, v in (("status", status), ("district", district), ("subdivision", subdivision), ("village", village)):
        if v: conds.append({k: v})
    if search:
        rx = {"$regex": re.escape(search), "$options": "i"}
        conds.append({"$or": [{"claimId": rx}, {"village": rx}, {"claimant": rx}, {"gramSabha": rx}]})
    if from_date or to_date:
        conds.append({"createdAt": {**({"$gte": from_date} if from_date else {}), **({"$lte": to_date} if to_date else {})}})
    q = {"$and": conds}
    total = await db().claims.count_documents(q)
    rows = await db().claims.find(q, {"_id": 0}).sort("updatedAt", -1).skip((page - 1) * page_size).limit(page_size).to_list(page_size)
    return ok(rows, pagination={"page": page, "limit": page_size, "total": total, "totalPages": -(-total // page_size)})

@router.get("/claims/{cid}")
async def claim(cid: str, user=Depends(current_user)):
    c = await _claim(cid, user)
    c["allowedActions"] = allowed_actions(c["status"], user["role"])  # backend decides, UI renders
    return ok(c)

@router.get("/claims/{cid}/timeline")
async def timeline(cid: str, user=Depends(current_user)):
    await _claim(cid, user)
    return ok(await db().workflowEvents.find({"claimId": cid}, {"_id": 0}).sort("timestamp", 1).to_list(500))

@router.get("/claims/{cid}/audit")
async def audit(cid: str, user=Depends(current_user)):
    await _claim(cid, user)
    return ok(await db().auditLogs.find({"claimId": cid}, {"_id": 0}).sort("timestamp", 1).to_list(500))

class ActionIn(BaseModel):
    action: str
    remarks: Optional[str] = None

@router.post("/claims/{cid}/actions")
async def act(cid: str, b: ActionIn, user=Depends(current_user)):
    c = await _claim(cid, user)
    rule = TRANSITIONS.get(c["status"], {}).get(b.action)
    if not rule:
        raise err(409, "INVALID_TRANSITION", f"{b.action} is not valid from {c['status']}")
    to, roles, pending = rule
    if user["role"] not in roles:
        raise err(403, "FORBIDDEN", "Your role cannot perform this action")
    if b.action in REMARKS_REQUIRED and not (b.remarks or "").strip():
        raise err(422, "REMARKS_REQUIRED", "Remarks are required for this action")
    ev = {"claimId": cid, "actorId": user["email"], "actorName": user["name"], "actorRole": user["role"],
          "action": b.action, "fromStatus": c["status"], "toStatus": to, "remarks": b.remarks, "timestamp": now()}
    await db().workflowEvents.insert_one(dict(ev))
    await db().auditLogs.insert_one(dict(ev))  # append-only: no update/delete endpoints exist
    await db().claims.update_one({"claimId": cid}, {"$set": {"status": to, "pendingWith": pending, "updatedAt": ev["timestamp"]}})
    return ok(await _claim(cid, user), "Action recorded")
