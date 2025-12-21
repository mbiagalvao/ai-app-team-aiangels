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

print(update_profile("69481a50c3bfe0a238773d70", {"city": "Madrid", "country": "Spain"}))

print(delete_profile("6948192f9edec5b018156375"))

