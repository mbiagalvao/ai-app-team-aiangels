"""
weather_report.py - Create a weather report with current conditions and a 3 day forecast.
Article of inspiration used: https://dimasyotama.medium.com/build-an-ai-powered-weather-api-with-python-flask-openweathermap-and-gemini-8e5cbf87af5d
API service: https://openweathermap.org/
"""
import httpx
import logging
from langfuse import observe
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from utils.prompt import PromptLoader

prompts = PromptLoader()

load_dotenv()

OWM_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key = GOOGLE_API_KEY)

logger = logging.getLogger("WeatherReportService")
logger.setLevel(logging.INFO)

class WeatherReportService:
    def __init__(self, own_api_key = OWM_API_KEY):
        self.client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
        self.own_api_key = own_api_key
        self.google_api_key = GOOGLE_API_KEY
        self.prompts = PromptLoader()

    @observe(as_type="tool")
    def get_owm_forecast(self, location: str) -> dict:
        """
        Fetch 5-day forecast for a city by first fetching its coordinates.
        """
        try:
            #Get latitude and longitude
            current_url = "http://api.openweathermap.org/data/2.5/weather"
            params = {'q': location, 'appid': self.own_api_key, 'units': 'metric'}

            with httpx.Client() as wclient:
                response = wclient.get(current_url, params=params)
                response.raise_for_status()
            weather_data = response.json()
            lat = weather_data['coord']['lat']
            lon = weather_data['coord']['lon']

            # Step 2: Fetch forecast using coordinates
            forecast_url = "http://api.openweathermap.org/data/2.5/forecast"
            params_forecast = {'lat': lat, 'lon': lon, 'appid': self.own_api_key, 'units': 'metric'}

            with httpx.Client() as wclient:
                response = wclient.get(forecast_url, params=params_forecast)
                response.raise_for_status()
            return response.json()

        except httpx.HTTPStatusError as e:
            logger.error(f"HTTPStatusError fetching forecast for {location}: {e}")
            raise
        except httpx.RequestError as e:
            raise Exception(f"Network error connecting to OpenWeatherMap for forecast: {e}")
       
    def get_gemini_summary(self, weather_data_str):
        if not self.google_api_key:
            logger.warning("GEMINI_API_KEY not set. Skipping summary.")
            return "AI summary feature disabled: Google API key not set."
    
        system_prompt = prompts.load("weather_system")
        
        try:
            response = self.client.models.generate_content(
                model = "gemini-2.5-flash",
                contents= weather_data_str,
                config=types.GenerateContentConfig(
                    temperature=0.1,
                    system_instruction=system_prompt,
                )
            )
        
            return response.text
    
        except Exception as e:
            logger.error(f"Error with Gemini API: {e}")
            return "Summary currently unavailable due to an error."