from fastapi import FastAPI
from app.routes import auth, users
from app.core.logging_config import setup_logging
from app.database import init_db

app = FastAPI(title="User Authentication System")

@app.on_event("startup")
async def startup_event():
    setup_logging()
    await init_db()

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/users", tags=["Users"])
