"""
todo_lists.py - Create a to-do list for a given natural disaster or emergency and a given location.
"""

from langfuse import observe
from utils.prompt import PromptLoader
from google import genai
from google.genai import types

prompts = PromptLoader()
client = genai.Client()
model_name = "gemini-2.5-flash"

@observe(as_type="tool")
def todo_list_tool(disaster_type: str, message: str, location: str = None, context: str = None) -> str:
    """
    Use this tool ONLY when asked by the user to create a to-do list
    for a specific disaster or emergency. This could be for before, during or after the event.
    Extract the disaster type and location from the user message if not provided.
    Extract the context from the vector DB if available.
    The message is the user query for a to-do list (disaster type included in the message).

    Args:
        disaster_type: Type of natural disaster or emergency (e.g., "earthquake", "fire")
        message: User query for a to-do list (disaster type included in the message)
        location: Optional location string
        context: Optional context (possibly retrieved from the vector DB)
    
    Returns:
        To-do list as a string
    """
    system_prompt = prompts.format(
            "to_do_list_system",
            disaster_type= disaster_type)

    # Format context section
    user_prompt = message
    if context:
        user_prompt = f"{message}\n\nRELEVANT CONTEXT:\n{context}"
        
    try:
        response = client.models.generate_content(
            model = model_name,
            contents=user_prompt,
            config=types.GenerateContentConfig(
                temperature=0.2,
                system_instruction=system_prompt
            )
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"