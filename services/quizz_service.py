"""
quizz_service.py - Service for generating quizzes based on a specific disaster type.
"""
import os
from dotenv import load_dotenv
import json
from google import genai
from google.genai import types
from utils.prompt import PromptLoader

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
model_name = "gemini-2.5-flash"

prompts = PromptLoader()

class QuizzService:
    def __init__(self, topic: str):
        self.topic = topic
    
    def generate_quizz(self, topic: str = None, questions: int = 5):
        if topic is None:
            topic = self.topic

        system_prompt = prompts.load("quiz_system")
        
        user_prompt = f"""Generate {questions} multiple choice questions about {topic}.

Return ONLY a valid JSON array with this exact format:
[
  {{
    "question": "Question text here?",
    "answers": ["Option 1", "Option 2", "Option 3", "Option 4"],
    "correct": 0
  }}
]

Where "correct" is the index (0-3) of the correct answer in the "answers" array.
Do not include any markdown formatting or extra text, just the JSON array."""

        response = client.models.generate_content(
            model=model_name,
            contents=user_prompt,
            config=types.GenerateContentConfig(
                temperature=0.7,
                system_instruction=system_prompt
            )
        )
        
        response_text = response.text.strip()
        
        if response_text.startswith("```"):
            lines = response_text.split("\n")
            response_text = "\n".join(lines[1:-1])
            if response_text.startswith("json"):
                response_text = response_text[4:].strip()
        
        print(f"CLEANED RESPONSE: {response_text[:200]}...")
        
        try:
            quiz_raw = json.loads(response_text)
            
            quiz = []
            for q in quiz_raw:
                answers = q.get("answers", [])
                
                # Remove "A. ", "B. ", etc if exists
                clean_answers = []
                for ans in answers:
                    if isinstance(ans, str) and len(ans) > 3 and ans[1:3] == ". ":
                        clean_answers.append(ans[3:])
                    else:
                        clean_answers.append(ans)
                
                quiz.append({
                    "question": q.get("question", ""),
                    "answers": clean_answers,
                    "correct": q.get("correct", 0)
                })
            
            print(f"CONVERTED {len(quiz)} questions successfully")
            return quiz
            
        except Exception as e:
            print(f"Error parsing quiz JSON: {e}")
            import traceback
            traceback.print_exc()
            
            quiz = [
                {
                    "question": f"Sample question {i+1} about {topic}",
                    "answers": ["Option A", "Option B", "Option C", "Option D"],
                    "correct": 0
                }
                for i in range(questions)
            ]
            return quiz
