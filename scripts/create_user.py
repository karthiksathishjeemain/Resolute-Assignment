import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.security import get_password_hash
from app.config import settings

async def create_admin_user():
    client = AsyncIOMotorClient(settings.mongodb_url)
    db = client.auth_db
    
    admin_user = {
        "email": "admin@example.com",
        "password": get_password_hash("admin123"),
        "role": "admin"
    }
    
    if not await db.users.find_one({"email": admin_user["email"]}):
        await db.users.insert_one(admin_user)
        print("Admin user created successfully")
    else:
        print("Admin user already exists")

if __name__ == "__main__":
    asyncio.run(create_admin_user())