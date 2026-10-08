from fastapi import APIRouter, Depends
from pydantic import BaseModel
from ..database import db
from ..security import check_pw, current_user, err, make_token

router = APIRouter(prefix="/auth", tags=["auth"])

class Login(BaseModel):
    email: str
    password: str

@router.post("/login")
async def login(b: Login):
    u = await db().users.find_one({"email": b.email.lower()})
    if not u or not check_pw(b.password, u["passwordHash"]):
        raise err(401, "BAD_CREDENTIALS", "Incorrect email or password")
    u.pop("_id"); u.pop("passwordHash")
    return {"success": True, "data": {"token": make_token(u), "user": u}, "message": "Logged in"}

@router.get("/me")
async def me(user=Depends(current_user)):
    return {"success": True, "data": user, "message": "OK"}

@router.post("/logout")
async def logout(user=Depends(current_user)):
    # Stateless JWT: client discards the token. Server-side revocation is a production TODO.
    return {"success": True, "data": None, "message": "Logged out"}
