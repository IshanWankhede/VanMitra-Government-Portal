from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from . import database
from .config import settings
from .routers import auth, government

@asynccontextmanager
async def lifespan(app):
    await database.connect()
    yield
    await database.close()

app = FastAPI(title="VanMitra Government Portal API (development)", lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=[o.strip() for o in settings.cors_origins.split(",")],
                   allow_methods=["*"], allow_headers=["*"])

@app.exception_handler(HTTPException)
async def http_err(_, e):
    d = e.detail if isinstance(e.detail, dict) else {"code": "ERROR", "message": str(e.detail)}
    return JSONResponse({"success": False, "error": d}, status_code=e.status_code)

app.include_router(auth.router, prefix="/api")
app.include_router(government.router, prefix="/api")
