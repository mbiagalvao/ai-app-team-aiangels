"""
embedder.py - embedding the extracted content from the pdfs for the RAG service
"""

import os
from google import genai
from google.genai import types
from langfuse import observe

class EmbeddingService:
    """
    Service for generating text embeddings using Google Gemini.
    
    Uses gemini-embedding-001 with configurable dimensions.
    """
    
    def __init__(self, output_dimensionality: int = 768):
        """Initialize the embedding service.
        
        Args:
            output_dimensionality: Number of dimensions (128-3072)
                                 Default: 768 (optimal balance)
        """
        self.client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = "gemini-embedding-001"
        self.output_dimensionality = output_dimensionality
    
    @observe(as_type="embedding")
    def generate_embedding(self, text: str) -> list[float]:
        """Generate an embedding for the given text.
        
        Args:
            text: Input text (max 2,048 tokens)
            
        Returns:
            List of floats representing the embedding
        """
        if not text or not text.strip():
            raise ValueError("Text cannot be empty")
        
        result = self.client.models.embed_content(
            model=self.model,
            contents=text,
            config=types.EmbedContentConfig(
                output_dimensionality=self.output_dimensionality
            )
        )
        
        return result.embeddings[0].values