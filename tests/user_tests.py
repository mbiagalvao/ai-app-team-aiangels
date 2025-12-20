import os
from dotenv import load_dotenv
from pymongo import MongoClient
from rag.vector_search import vector_search
from services.user_creation import create_profile, users_collection

new_user = create_profile(name="Inês", email="test@example.com", country="Portugal", city="Lisbon", age=30)

print("Created user_id:", new_user.user_id)

stored = users_collection.find_one({"user_id": new_user.user_id})
print("Stored document:", stored)