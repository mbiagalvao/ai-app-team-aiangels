import os
from dotenv import load_dotenv
import google.generativeai as genai


class AIClient:
    """Simple client for Google Gemini API"""

    def __init__(self):
        # Load environment variables
        load_dotenv()

        # Get API key
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")

        # Configure the API
        genai.configure(api_key=api_key)

        # Create model
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def chat(self, message):
        """Send a message to AI and get response"""
        try:
            response = self.model.generate_content(message)
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


# Test the client
if __name__ == "__main__":
    try:
        client = AIClient()
        response = client.chat("Hello! Tell me a fun fact about AI.")
        print(f"AI Response: {response}")
    except Exception as e:
        print(f"Error: {e}")