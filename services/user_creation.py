"""
user_creation.py - User creation for chatbot application
"""
from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["catastrophe_db"]
users_collection = db["users"]
users_collection.create_index("user_id", unique = True)

class User:
    def __init__(self, user_id: str, name: str, email: str, country: str, city: str, age: int | None = None):
        """
        Initialize User
        
        Args:
            user_id: Unique identifier for the user
            name: Name of the user
            email: Email address of the user
            country: Country where the user is located
            city: City where the user is located
            age: Age of the user - optional
        """
        self.user_id = user_id
        self.name = name
        self.email = email
        self.country = country
        self.city = city
        self.age = age

    def transform_to_dict(self): # transform to dictionary to be received in mongo db
        return {"user_id": self.user_id,
                "name": self.name,
                "email": self.email,
                "country": self.country,
                "city": self.city,
                "age": self.age}

def create_profile(name: str, email: str, country: str, city: str, age: int | None = None):
    profile = User(name = name, email = email, country = country, city = city, age = age)
    results = users_collection.insert_one(profile.transform_to_dict()) # does this effectively insert the user into the mongodb col?
    return results.inserted_id

def update_profile(user_id: str, fields: dict):
    allowed_fields = {"name", "email", "country", "city", "age"} # user_id is unchangeable
    update_dict = {k: v for k, v in fields.items() if k in allowed_fields}
    if not update_dict:
        raise ValueError("No valid fields to update")
    results = users_collection.update_one({"user_id": user_id}, {"$set": update_dict})
    if results.matched_count == 0:
        raise ValueError("Profile not found")

def delete_profile(user_id: str):
    users_collection.delete_one({"user_id": user_id}) # returns None if there is no profile with that user_id
