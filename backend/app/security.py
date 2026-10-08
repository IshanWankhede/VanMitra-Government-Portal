import bcrypt, jwt
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from .config import settings
from .database import db

bearer = HTTPBearer(auto_error=False)

def err(status, code, message):
    return HTTPException(status, {"code": code, "message": message})

def hash_pw(p): return bcrypt.hashpw(p.encode(), bcrypt.gensalt()).decode()
def check_pw(p, h): return bcrypt.checkpw(p.encode(), h.encode())

def make_token(user):
    exp = datetime.now(timezone.utc) + timedelta(minutes=settings.jwt_expire_minutes)
    return jwt.encode({"sub": user["email"], "exp": exp}, settings.jwt_secret, algorithm="HS256")

async def current_user(cred: HTTPAuthorizationCredentials = Depends(bearer)):
    if not cred:
        raise err(401, "UNAUTHENTICATED", "Login required")
    try:
        email = jwt.decode(cred.credentials, settings.jwt_secret, algorithms=["HS256"])["sub"]
    except jwt.PyJWTError:
        raise err(401, "INVALID_TOKEN", "Session expired or invalid")
    user = await db().users.find_one({"email": email}, {"_id": 0, "passwordHash": 0})
    if not user:
        raise err(401, "INVALID_TOKEN", "User not found")
    return user
