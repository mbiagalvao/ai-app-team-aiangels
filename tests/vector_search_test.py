"""
vector_search_test.py - Test script for vector search functionality.
"""
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from rag.vector_search import vector_search

load_dotenv()

mongo_uri = os.getenv("MONGODB_URI")

if mongo_uri:
    client = MongoClient(mongo_uri)
    db = client["catastrophe_db"]
    collection = db["documents"]

    # Test Query 1: Account access issue
    query = "O que fazer na preparação numa inundação?"
    print(f"🔍 Query: '{query}'\n")
    
    results = vector_search(collection, query, limit=3)
    
    print(f"📊 Found {len(results)} similar tickets:\n")
    for i, result in enumerate(results, 1):
        score = result['score']
        text = result['text']
        category = result['metadata']['category']
        
        print(f"  {i}. Similarity: {score:.3f}")
        print(f"     Text: {text}")
        print(f"     Category: {category}\n")
    
    print("💡 Notice: It found documents disaster related even though")
    print("   the query doesn't use the exact words!")
else:
    print("⚠️ Skipping search test (no MongoDB connection)")