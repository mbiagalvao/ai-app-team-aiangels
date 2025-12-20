"""
quizz_service.py - Service for generating quizzes based on a specific disaster type.
"""
import json
from google import genai
from google.genai import 
from google.genai import types
from utils.prompt import PromptLoader

client = genai.Client()
model_name = "gemini-2.5-flash"

prompts = PromptLoader()

class QuizzService:
    def __init__(self, topic: str):
        self.topic = topic
    
    def generate_quizz(self, topic: str, level:str = "medium", questions: int = 5):
        """
        Generate quizzes dynamically based on a specific disaster type.

        Args:
            disaster_type: Type of disaster to generate questions about
            questions: Number of questions to generate (default is 5)

        Returns:
            List of generated quiz questions in a structured format
        """

        system_prompt = prompts.load("quiz_system")
    
        response_text = response = client.models.generate_content(
            model = model_name,
            config=types.GenerateContentConfig(
                temperature=0.2,
                system_instruction=system_prompt
            )
        )
  
        try:
            quiz = json.loads(response_text)
        except Exception:
            # Fallback if parsing fails
            quiz = [
                {"question": f"Sample question {i+1}", "options": ["A","B","C","D"], "answer": "A"}
                for i in range(questions)
            ]
        return quiz