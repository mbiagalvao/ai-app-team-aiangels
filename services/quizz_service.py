"""
quizz_service.py - Service for generating quizzes based on a specific disaster type.
"""
import json
from services.ai_client import AIClient

class QuizzService:
    def __init__(self, disaster_type: str):
        self.disaster_type = disaster_type
        self.ai_client = AIClient()
    
    def generate_quizz(self, disaster_type: str, questions: int = 5):
        """
        Generate quizzes dynamically based on a specific disaster type.

        Args:
            disaster_type: Type of disaster to generate questions about
            questions: Number of questions to generate (default is 5)

        Returns:
            List of generated quiz questions in a structured format
        """

        system_prompt = """
            You are an expert in quizzes about natural disasters and emergencies.
            Generate a multiple-choice quiz with {questions} questions about {disaster_type}.
            Each question should have 4 options (A, B, C, D) and indicate the correct answer.

            Format the output as the following JSON structure:
            [
            {{
                "question": "Question text",
                "options": ["A", "B", "C", "D"],
                "answer": "A"
            }},
            ...
            ]
        """
    
        response_text = self.ai_client.generate_text(system_prompt)
  
        try:
            quiz = json.loads(response_text)
        except Exception:
            # Fallback if parsing fails
            quiz = [
                {"question": f"Sample question {i+1}", "options": ["A","B","C","D"], "answer": "A"}
                for i in range(questions)
            ]
        return quiz