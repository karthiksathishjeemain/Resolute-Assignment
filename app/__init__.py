from fastapi import FastAPI
from app.routes import auth, users
from app.core.logging_config import setup_logging

def create_app() -> FastAPI:
    """Create and configure the FastAPI application"""
    app = FastAPI(
        title="User Authentication System",
        description="A secure authentication system with RBAC support",
        version="1.0.0"
    )
 
    app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
    app.include_router(users.router, prefix="/users", tags=["Users"])
    
    return app
