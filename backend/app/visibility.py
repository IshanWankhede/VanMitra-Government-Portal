"""Role-scoped visibility. Enforced here (backend), never only in the UI.
inbox   = claims waiting on this role.
handled = claims this role already acted on.
all     = everything (admin only)."""
from .database import db
from .security import err
from .workflow import inbox_states

async def scope_query(user, scope):
    role = user["role"]
    if scope == "all":
        if role != "GOVERNMENT_ADMIN":
            raise err(403, "FORBIDDEN", "Only admin can view all claims")
        return {}
    inbox = {"status": {"$in": inbox_states(role)}}
    if scope == "inbox":
        return inbox
    ids = await db().workflowEvents.distinct("claimId", {"actorId": user["email"]})
    handled = {"claimId": {"$in": ids}}
    if scope == "handled":
        return handled
    return {"$or": [inbox, handled]}  # "visible"

async def can_see(user, claim_id):
    if user["role"] == "GOVERNMENT_ADMIN":
        return True
    q = await scope_query(user, "visible")
    return await db().claims.count_documents({"$and": [{"claimId": claim_id}, q]}) > 0
