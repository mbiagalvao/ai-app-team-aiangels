"""
rag.py - Retrieval-Augmented Generation (RAG) implementation using Google GenAI and MongoDB
"""
import os
from dotenv import load_dotenv
from rag.vector_search import vector_search
from rag.embedding_service import EmbeddingService
from google import genai
from google.genai import types
from utils.prompt import PromptLoader
from pymongo import MongoClient

load_dotenv()

#initialize GenAI client
client = genai.Client()
model_name = "gemini-2.5-flash"

prompts = PromptLoader()

#initialize MongoDB client
mongo_uri = os.getenv("MONGODB_URI")
client = MongoClient(mongo_uri)
db = client["catastrophe_db"]
documents = db["documents"]

def run_rag(query: str, collection=documents) -> dict:
    """
    Run Retrieval-Augmented Generation.

    Args:
        query: User query string
        collection: MongoDB collection
        embedding_service: instance of your embedding service
        llm: your initialized LLM client
        top_k: number of relevant documents to retrieve

    Returns:
        Dictionary with "answer" and "sources"
    """

    results = vector_search(collection, query)

    system_prompt = prompts.load("rag_system")
    
    try:
        response = client.models.generate_content(
            model = model_name,
            config=types.GenerateContentConfig(
                temperature=0.0,
                system_instruction=system_prompt
            )
        )
        return {
        "answer": response,
        "sources": results
    }
    except Exception as e:
        return f"Error: {str(e)}"