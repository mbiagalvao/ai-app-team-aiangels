import os
from dotenv import load_dotenv
from google import genai
from google.genai import errors, types

# Load environment variables from .env file
load_dotenv()

#defining the model to be used
DEFAULT_MODEL = "gemini-2.5-flash-lite"

client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

## Testing the connection
print("🔄 Testing connection...")
try:
    response = client.models.generate_content(
        model=DEFAULT_MODEL,
        contents="Reply with 'Ready for advanced prompting!'"
    )
    print("✅", response.text)
except Exception as e:
    print(f"❌ Error: {e}")
    print("💡 Check your API key and internet connection")


# Example prompt for emergency and natural disaster advice
prompt = "What should I do in case of an earthquake? I am based in Lisbon, Portugal."
response = client.models.generate_content(
    model=DEFAULT_MODEL,
    contents=prompt,
    config=types.GenerateContentConfig(
        system_instruction="""You are a helpful emergencies and natural disasters' specialist.
    Your job is to:
    - Provide to-do list steps based on the given emergency or natural disaster scenario.
    - Provide emergency meeting points based on the user's location.

    Be clear, concise and calming in your responses.""",
        temperature=0.5,
    ),
)
print("Response:", response.text)