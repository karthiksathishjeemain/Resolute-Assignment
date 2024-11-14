from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user import Token
from app.core.security import create_access_token, verify_password
from app.database import get_database
from loguru import logger

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(email: str, password: str):
    db = await get_database()
    user = await db.users.find_one({"email": email})
    
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    
    access_token = create_access_token(
        data={"sub": str(user["_id"]), "email": email, "role": user["role"]}
    )
    logger.info(f"User {email} logged in successfully")
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/logout")
async def logout():
    # In a real implementation, you might want to blacklist the token
    return {"message": "Successfully logged out"}