"""
user_creation.py - User creation for chatbot application
"""

import os
from dotenv import load_dotenv
from pymongo import MongoClient
from rag.embedder import EmbeddingService
from rag.loader import extract_pdf
from langchain_text_splitters import RecursiveCharacterTextSplitter
load_dotenv()  # Load environment variables from .env file

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
    
    def create_profile(self, user_id: str, name: str, email: str, country: str, city: str, age: int | None = None):
        if self.repo.get(user_id):
            raise ValueError("Profile already exists")
        profile = User(user_id = user_id, name = name, email = email, country = country, city = city, age = age)
        self.repo.save(profile)
        return profile
    
    def update_profile(self, user_id: str, fields: dict):
        allowed_fields = {"name", "email", "country", "city", "age"}
        update = {k: v for k, v in fields.items() if k in allowed_fields}
        if not update:
            raise ValueError("No valid fields to update")
        updated = self.repo.update_fields(user_id, update)
        if not updated:
            raise ValueError("Profile not found")
        return self.get_profile(user_id)
    
    def delete_profile(self, user_id: str):
        self._store.pop(user_id, None) # Returns None if there is no profile with that user_id


def storing_user_in_mongodb(user_id: str, collection):
    """
    Store document chunks with embeddings into MongoDB.

    Args:
        file_path: Path to the PDF file.
        collection: MongoDB collection to store documents.
    """
    extracted_pages = extract_pdf(file_path)

    full_text = ""

    for page in extracted_pages:
        full_text += page["text"] + "\n"
    
    #chunking the text
    splitter = RecursiveCharacterTextSplitter(full_text, chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_text(full_text)

    docs = []
    for chunk_id, chunk in enumerate(chunks):
        embedding = service.generate_embedding(chunk)
        
        docs.append({
            "document_id": os.path.basename(file_path),
            "chunk_id": chunk_id,
            "text": chunk,
            "embedding": embedding,
            "metadata": {
                "category": "general",
                "source": "pdf"
            }
        })

    if docs:
        collection.insert_many(docs)
        print(f"✅ Inserted {len(docs)} documents into MongoDB from {file_path}")