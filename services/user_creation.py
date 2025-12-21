"""
user_creation.py - User creation for chatbot application
"""
from pymongo import MongoClient
import os
from bson import ObjectId
from dotenv import load_dotenv

load_dotenv()
MONGODB_URI = "mongodb+srv://biadgalvao:1AxYJ1OScM2hnank@cluster0.0cg8hoz.mongodb.net/?appName=Cluster0"
client = MongoClient(os.getenv("MONGODB_URI"))
db = client["catastrophe_db"]
users_collection = db["users"]

class User:
    def __init__(self, name: str, email: str, country: str, city: str, age: int | None = None):
        """
        Initialize User
        
        Args:
            name: Name of the user
            email: Email address of the user
            country: Country where the user is located
            city: City where the user is located
            age: Age of the user - optional
        """
        self.name = name
        self.email = email
        self.country = country
        self.city = city
        self.age = age

    def transform_to_dict(self): # transform to dictionary to be received in mongo db
        return {"name": self.name,
                "email": self.email,
                "country": self.country,
                "city": self.city,
                "age": self.age}

def create_profile(name: str, email: str, country: str, city: str, age: int | None = None):
    profile = User(name = name, email = email, country = country, city = city, age = age)
    results = users_collection.insert_one(profile.transform_to_dict()) # does this effectively insert the user into the mongodb col?
    return results.inserted_id

def get_profile(user_id: str) -> dict:
    profile = users_collection.find_one({"_id": ObjectId(user_id)})
    if not profile:
        raise ValueError("Profile not found")
    profile["_id"] = str(profile["_id"])
    return profile

def update_profile(user_id: str, fields: dict):
    allowed_fields = {"name", "email", "country", "city", "age"} # user_id is unchangeable
    update_dict = {k: v for k, v in fields.items() if k in allowed_fields}
    if not update_dict:
        raise ValueError("No valid fields to update")
    results = users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_dict})
    if results.matched_count == 0:
        raise ValueError("Profile not found")

def delete_profile(user_id: str):
    users_collection.delete_one({"_id": ObjectId(user_id)}) # returns None if there is no profile with that user_id
