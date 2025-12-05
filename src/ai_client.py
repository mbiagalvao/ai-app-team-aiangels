"""
ai_client.py - Client creation for Google Gemini API using google-generativeai library.
"""

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from langfuse import observe
from utils import PromptLoader

load_dotenv()

class AIClient:
    """Simple client for Google Gemini API"""

    def __init__(self, model_name: str = "gemini-2.5-flash"):
        """Initialize AI client
        
        Args:
            model: Gemini model to use (default is "gemini-2.5-flash-lite")
        """

        self.client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model_name = model_name
        self.prompts = PromptLoader()
        self.chat_history = []


    @observe(as_type="generation")
    def answer_question(self, message: str, use_history: bool = True):
        """
        Answer question realted to a specific natural disaster or emergency.

        Args:
            message: User question about natural disaster or emergency
            use_history: Whether to use chat history for context (default is True)

        Returns:
            Answer to the user's question
        """
        system_prompt = self.prompts.format(
                            "answer_question_system",
                            disaster = self.extract_disaster_type(message),
                            location = self.extract_location(message)
        )

        try:
            if use_history and self.chat_history:
                convo_context = "\n".join(self.chat_history[-10:])
                full_message = f"{convo_context}\nUser: {message}"
            else:
                full_message = message

            response = self.client.models.generate_content(
                model = self.model_name,
                contents= full_message,
                config=types.GenerateContentConfig(
                    temperature=0.5,
                    system_instruction=system_prompt
                )
            )

            #appeding to chat history
            if use_history:
                self.chat_history.append(f"User: {message}")
                self.chat_history.append(f"AI: {response.text}")
                
                #limiting the size of the chat history to the last 15 messages
                if len(self.chat_history) > 15:
                    self.chat_history = self.chat_history[-15:]
            
            return response.text
        
        except Exception as e:
            return f"Error: {str(e)}"
  

    @observe(as_type="generation")
    def extract_disaster_type(self, message: str) -> str:
        """
        Extract disaster type from the message
        
        Args:
            message: User message
        
        Returns:
            Extracted disaster type as a string
    """
        extraction_prompt = f"""
            Identify the type of natural disaster or emergency mentioned in the message. Return only the disaster type in lowercase (e.g. "earthquake", "flood", "hurricane"). If no specific disaster is mentioned, return "general emergency".
        
            Message: "{message}"
            Disaster Type:
        """
        try:
            response = self.client.models.generate_content(
                model = self.model_name,
                contents = extraction_prompt,
            generation_config=types.GenerateContentConfig(temperature=0.0)
            )

            return response.text.strip().lower()
        
        except Exception as e:
            return "general emergency"

    @observe(as_type="generation")
    def extract_location(self, message: str) -> str:
        """
        Extract the user's location from the message
        
        Args:
            message: User message
        
        Returns:
            Extracted location as a string
    """
        extraction_prompt = f"""
            Identify the location of the user mentioned in the message. Return only the location (e.g. "Lisboa", "New York", "London"). If no specific location is mentioned, return "unknown".
        
            Message: "{message}"
            Location:
        """
        try:
            response = self.client.models.generate_content(
                model = self.model_name,
                contents = extraction_prompt,
            generation_config=types.GenerateContentConfig(temperature=0.0)
            )

            return response.text.strip().lower()
        
        except Exception as e:
            return "unknown"
    
    @observe(as_type="span") #it is not a generation but we want to track if it is successfully called
    def reset_chat_history(self):
        """Reset the chat history"""
        self.chat_history = []
        return "Chat history cleared."