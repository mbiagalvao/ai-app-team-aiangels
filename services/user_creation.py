"""
user_creation.py - User creation for chatbot application
"""

from pymongo import MongoClient
import os
mongo_uri = os.getenv("MONGODB_URI")
client = MongoClient(mongo_uri)
db = client["catastrophe_db"]
documents = db["documents"]

class User:
    def __init__(self, user_id: str, name: str, email: str, country: str, city: str, age: int | None = None):
        """
        Initialize User
        
        Args:
            user_id: Unique identifier for the user
            name: Name of the user
            email: Email address of the user
            country: Country where user is located
            city: City where user is located
            age: Age of the user - optional
        """
        self.user_id = user_id
        self.name = name
        self.email = email
        self.country = country
        self.city = city
        self.age = age

def create_profile(self, user_id: str, name: str, email: str, country: str, city: str, age: int | None = None) -> User:
    if self.repo.get(user_id):
        raise ValueError("Profile already exists")
    profile = User(user_id = user_id, name = name, email = email, country = country, city = city, age = age)
    self.repo.save(profile)
    return profile
    
def get_profile(self, user_id: str) -> User:
    profile = self.repo.get(user_id)
    if not profile:
        raise ValueError("Profile not found")
    return profile

def update_profile(user_id, fields: dict) -> User:
    allowed_fields = {"name", "email", "country", "city", "age"}
    for key, value in fields.items():
        if key in allowed_fields:
            profile = get_profile(user_id)
            setattr(profile, key, value)
