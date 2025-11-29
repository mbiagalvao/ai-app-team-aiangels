"""
ai_client.py - Client creation for Google Gemini API using google-generativeai library.
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.genai import errors, types
from langfuse import observe
from utils.prompts import PromptLoader


class AIClient:
    """Simple client for Google Gemini API"""

    def __init__(self, model: str = "gemini-2.5-flash-lite"):
        """Initialize AI client
        
        Args:
            model: Gemini model to use (default is "gemini-2.5-flash-lite")
        """
        # Load environment variables
        load_dotenv()

        self.client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model_name = model
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
        system_instruction = self.prompts.load("answer_question_system")
        try:
            if use_history and self.chat_history:
                convo_context = "\n".join(self.chat_history[-10:])
                full_message = f"{convo_context}\nUser: {message}"
            else:
                full_message = message

            response = self.client.models.generate_content(
                contents=full_message,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    temperature=0.5,
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
    def to_do_list(self, message: str, context: str=None):
        """
        Generate a to-do list for a given natural disaster or emergency.
        
        Args:
            message: User request for a to-do list (disaster type included in the message)
            context: Optional context (possibly retrieved from the vector DB)

        Returns:
            To-do list as a string    
        """
        disaster_type = self.extract_disaster_type(message)

        system_instruction = self.prompts.format(
            "to_do_list_system",
            disaster= disaster_type)

        # Format context section
        user_prompt = message
        if context:
            user_prompt = f"{message}\n\nRELEVANT CONTEXT:\n{context}"
        
        try:
            response = self.model.generate_content(
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    temperature=0.2,
                )
            )
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"


    def chat_with_history(self, messages):
        """Chat with conversation history (list of messages)"""
        try:
            chat = self.model.start_chat(history=[])
            response = chat.send_message(messages[-1])  # Send latest message
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
                config=types.GenerateContentConfig(
                    temperature=0.0,
                )
            )
            return response.text.strip().lower()
        
        except Exception as e:
            return "general emergency"

    
    @observe(as_type="event") #it is not a generation but we want to track if it is successfully called
    def reset_chat_history(self):
        """Reset the chat history"""
        self.chat_history = []
