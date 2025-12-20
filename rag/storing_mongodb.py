"""
storing_mongodb.py - Store document chunks with embeddings into MongoDB documents' collection
"""

import os
from dotenv import load_dotenv
from pymongo import MongoClient
from rag.embedder import EmbeddingService
from rag.loader import extract_pdf
from langchain_text_splitters import RecursiveCharacterTextSplitter
load_dotenv()  # Load environment variables from .env file

service = EmbeddingService()

def storing_mongodb(file_path: str, collection):
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
    