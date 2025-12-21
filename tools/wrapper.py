"""
wrapper.py - Wrapper functions for built-in and custom tools' integration to be used by the AI client.
"""

from google import genai
from importlib_metadata import metadata
from google.genai import types
from langfuse import observe
from services.quizz_service import QuizzService
from rag.rag import run_rag
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

#initialize MongoDB client
mongo_uri = os.getenv("MONGODB_URI")
client = MongoClient(mongo_uri)
db = client["catastrophe_db"]
documents = db["documents"]


#Wrapper function that internally uses Google Search built-in tool
client = genai.Client()
quiz_service = QuizzService(topic="natural disasters")

#Search the web for current information
@observe(as_type="tool")
def web_search_tool(query: str) -> dict:
    """
    Use this tool ONLY when the user asks for current, up-to-date or
    external information (i.e. news, real-time updates and current events).
    DO NOT use this tool to create to-do-lists or calculate resources.
    DO NOT use this tool for generic questions that can be answered without web search.
    
    Args:
        query: The search query given by the user.
    
    Returns:
        Dictionary with 'answer' string and 'sources' list of sources.
    """
    print(f"[Searching: {query}]")

    response = client.models.generate_content(
        model= "gemini-2.5-flash",
        contents=f"Search for: {query}",
        config=types.GenerateContentConfig(
                  tools=[{"google_search": {}}]
                )
    )

    # Extract sources if available
    sources = []
    metadata = response.candidates[0].grounding_metadata
    if metadata and metadata.grounding_chunks:
        sources = [{"title": c.web.title, "url": c.web.uri}
                        for c in metadata.grounding_chunks]
    
    return {"answer": response.text, "sources": sources}


#Obtain weather information for a specific location
@observe(as_type="tool")
def weather_tool():
    return "Weather tool placeholder"


#Generate quizzes about specific disaster types
@observe(as_type="tool")
def quizz_wrapper_tool(topic: str, level: str = "medium"):
    """
    Generate quizzes about specific disaster types.
    
    ALWAYS use this tool if the user requests:
    - a quiz
    - a test
    - practice questions
    - multiple-choice questions
    about a specific disaster or emergency.
    
    If the user does not specify a topic, tell them to try out the "Quizzes page".
    Extract the topic and level from the user's question.
    If the user does not specify a level, use "medium" as default.

    Args:
        topic: Topic for the quiz (e.g., "earthquakes", "floods")
        level: Difficulty level of the quiz ("easy", "medium", "hard")
    
    Returns:
        Generated quiz as a string
    """
    if not topic:
        raise ValueError("Topic is required")

    quiz = quiz_service.generate_quizz(
        topic=topic,
        level=level,
    )

    return quiz


#RAG tool wrapper for agent
@observe(as_type="tool")
def rag_tool(query: str) -> str:
    """
    RAG tool wrapper for agent.
    Use this tool ONLY to get context for your answers IF NECESSARY for crucial information.
    (i.e., asking for meeting points in Lisbon during an earthquake).
    Do NOT use this tool for generic questions that do not require specific context.

    Args:
        query: user question

    Returns:
        Answer string from RAG
    """
    result = run_rag(query=query, collection=documents)
    return result["answer"]
