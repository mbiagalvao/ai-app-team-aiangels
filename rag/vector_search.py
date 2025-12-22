"""
vector_search.py - perform vector search in MongoDB collection using embeddings.
"""

import os
from pymongo import MongoClient
from rag.embedder import EmbeddingService
from pymongo.collection import Collection
from langfuse import observe

mongo_uri = os.getenv("MONGODB_URI")

@observe(as_type="retrieve")
def vector_search(collection: Collection, query_text: str, limit: int = 5):
    embedding_service = EmbeddingService()

    query_embedding = embedding_service.generate_embedding(query_text)

    pipeline = [
        {
            "$vectorSearch": {
                "index": "vector_index",
                "path": "embedding",
                "queryVector": query_embedding,
                "numCandidates": 50,
                "limit": limit
            }
        },
        {
            "$project": {
                "_id": 0,
                "text": 1,
                "metadata": 1,
                "score": { "$meta": "vectorSearchScore" }
            }
        }
    ]

    results = list(collection.aggregate(pipeline))
    return results
