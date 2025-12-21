"""
ai_client.py - Main agent client for interacting with Google Gemini API.
"""

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from langfuse import observe
from utils.prompt import PromptLoader
#from tools.todo_lists import ToDoList
#from tools.resources_needed import ResourcesCalculator
from tools.wrapper import  web_search_tool, weather_tool, rag_tool
from tools.resources_needed import resources_calculator_tool
from tools.todo_lists import todo_list_tool

load_dotenv()

class AIClient:
    """Simple client for Google Gemini API"""

    def __init__(self, model_name: str = "gemini-2.5-flash"):
        """Initialize AI client
        
        Args:
            model: Gemini model to use (default is "gemini-2.5-flash")
        """

        self.client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model_name = model_name
        self.prompts = PromptLoader()
        self.chat_history = []
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.weather_api = os.getenv("OPENWEATHERMAP_API_KEY")


    @observe(as_type="agent")
    def answer_question(self, message: str, use_history: bool = True):
        """
        Answer question realted to a specific natural disaster or emergency.

        Args:
            message: User question about natural disaster or emergency
            use_history: Whether to use chat history for context (default is True)

        Returns:
            Answer to the user's question
        """
        #disaster_type = self.extract_disaster_type(message)
        #location = self.extract_location(message)
        
        #initialize tools
        #self.todo_list = ToDoList(disaster_type=disaster_type, location=location)
        #self.resources = ResourcesCalculator(disaster_type=disaster_type)

        system_prompt = self.prompts.load(
                            "answer_question_system"
                            #disaster =disaster_type,
                            #location = location
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
                    system_instruction=system_prompt,
                    tools = [todo_list_tool, resources_calculator_tool, web_search_tool, rag_tool, weather_tool]
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


    @observe(as_type="span") #it is not a generation but we want to track if it is successfully called
    def reset_chat_history(self):
        """Reset the chat history"""
        self.chat_history = []
        return "Chat history cleared."