from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user import UserCreate, UserUpdate, UserInDB
from app.core.security import get_current_user, get_password_hash
from app.database import get_database
from bson import ObjectId
from typing import List
from loguru import logger

router = APIRouter()

@router.get("/", response_model=List[UserInDB])
async def get_users(current_user: dict = Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Not enough privileges")
    
    db = await get_database()
    users = await db.users.find().to_list(length=100)
    return [UserInDB(**user) for user in users]

@router.post("/", response_model=UserInDB)
async def create_user(user: UserCreate, current_user: dict = Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Not enough privileges")
    
    db = await get_database()
    if await db.users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user_dict = user.dict()
    user_dict["password"] = get_password_hash(user_dict["password"])
    result = await db.users.insert_one(user_dict)
    
    logger.info(f"Created new user with email: {user.email}")
    return UserInDB(**user_dict, id=str(result.inserted_id))

# scripts/create_user.py
