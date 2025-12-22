"""
interactive_test.py - Interactive testing script for AIClient
"""
import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from langfuse import observe

load_dotenv()
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from services.ai_client import AIClient

def interactive_test():
    """Interactive testing script"""
    client = AIClient()
    
    print("🚨 Emergency AI Client - Interactive Test")
    print("=" * 60)
    print("\nSuggested test queries:")
    print("  1. What's the weather in Lisbon?")
    print("  2. I need emergency contacts in Porto")
    print("  3. Is Castelo Branco safe from earthquakes?")
    print("  4. What should I pack for a hurricane?")
    print("  5. Where can I evacuate in Coimbra?")
    print("\nType 'quit' to exit\n")
    
    while True:
        user_input = input("\n💬 You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break
        
        if not user_input:
            continue
        
        print("\n🤖 AI: ", end="", flush=True)
        response = client.answer_question(user_input)
        print(response)
        print("\n" + "-" * 60)

if __name__ == "__main__":
    interactive_test()