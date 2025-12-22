"""
rag_test.py - Tests for Retrieval-Augmented Generation (RAG) implementation
"""

import os
from dotenv import load_dotenv
from rag.rag import run_rag
from rag.vector_search import vector_search
from rag.embedder import EmbeddingService
from pymongo import MongoClient
load_dotenv()

mongo_uri = os.getenv("MONGODB_URI")
client = MongoClient(mongo_uri)
db = client["catastrophe_db"]
documents = db["documents"]

embedding_service = EmbeddingService()


query = "O que fazer na preparação para um sismo?"

# Run RAG
response = run_rag(query=query,collection=documents)
 
print("=== QUERY ===")
print(query)
print("\n=== ANSWER ===")
print(response)
print("\n=== SOURCES ===")
for i, src in enumerate(response.get("sources", []), 1):
    print(f"{i}. {src['text'][:100]}...")