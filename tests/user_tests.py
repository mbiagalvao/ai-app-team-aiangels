from pymongo import MongoClient
import os
from bson import ObjectId, SON
from dotenv import load_dotenv
from services.user_creation import (create_profile, get_profile, update_profile, delete_profile)

load_dotenv() # loads .env into process env

mongo_uri = os.getenv("MONGODB_URI")
if not mongo_uri:
    raise ValueError("⚠️ MONGODB_URI not found in environment variables")

mongo_client = MongoClient(mongo_uri)
db = mongo_client["catastrophe_db"]
users_collection = db["users"]

print("✅ Connected to MongoDB")

new_user_id = create_profile(name = "Inês", email = "test@example.com", country = "Portugal", city = "Lisbon", age = 30)
print(new_user_id)
