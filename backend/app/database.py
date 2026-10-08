from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings

_client = None

def db():
    return _client[settings.mongodb_database]

async def connect():
    global _client
    _client = AsyncIOMotorClient(settings.mongodb_uri)  # one client for the app lifetime
    d = db()
    await d.claims.create_index("claimId", unique=True)
    for f in ("status", "district", "subdivision", "village", "createdAt"):
        await d.claims.create_index(f)
    await d.workflowEvents.create_index("claimId")
    await d.auditLogs.create_index("claimId")
    await d.users.create_index("email", unique=True)

async def close():
    if _client:
        _client.close()
