"""
weather_report.py - Create a weather report with current conditions and a 3 day forecast.
Article of inspiration used: https://dimasyotama.medium.com/build-an-ai-powered-weather-api-with-python-flask-openweathermap-and-gemini-8e5cbf87af5d
API service: https://openweathermap.org/
"""
from langfuse import observe
import os
from utils.prompt import PromptLoader

OWM_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class WeatherReportService:
    def __init__(self, own_api_key = OWM_API_KEY):
        self.own_api_key = own_api_key
        self.gemini_api_key = GEMINI_API_KEY
        self.prompts = PromptLoader()

    def get_owm_weather(location):
        current_url = "http://api.openweathermap.org/data/2.5/weather"
        #Parameters for the API request
        params = {'q': location, 'appid': OWM_API_KEY, 'units': 'metric'}
        try:
            # Using httpx.Client as a context manager for efficient connection handling
            with httpx.Client() as client:
                response = client.get(current_url, params=params)
                response.raise_for_status() # Raises an HTTPStatusError for 4XX/5XX client/server errors
            return response.json() # Return the JSON response
        except httpx.HTTPStatusError as e:
            app.logger.error(f"HTTPStatusError fetching current weather for {location}: {e}")
            raise # Re-raise the exception to be handled by the main endpoint
        except httpx.RequestError as e:
            # For network errors, DNS failures, etc.
            app.logger.error(f"RequestError fetching current weather for {location}: {e}")
            raise Exception(f"Network error connecting to OpenWeatherMap: {e}")


    def get_owm_forecast(lat, lon):
        forecast_url = "http://api.openweathermap.org/data/2.5/forecast" # 5 day / 3 hour forecast
        params = {'lat': lat, 'lon': lon, 'appid': OWM_API_KEY, 'units': 'metric'}
        try:
            with httpx.Client() as client:
                response = client.get(forecast_url, params=params)
                response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            app.logger.error(f"HTTPStatusError fetching forecast for {lat},{lon}: {e}")
            raise
        except httpx.RequestError as e:
            app.logger.error(f"RequestError fetching forecast for {lat},{lon}: {e}")
            raise Exception(f"Network error connecting to OpenWeatherMap for forecast: {e}")
        
    def get_gemini_summary(weather_data_str):
    if not GEMINI_API_KEY:
        app.logger.warning("GEMINI_API_KEY not set. Skipping summary.")
        return "AI summary feature disabled: Gemini API key not set."
    
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        # Choose your preferred model. 'gemini-1.5-flash-latest' is a good, fast option.
        # The original code used 'gemini-2.0-flash-thinking-exp', which might be an internal or specific version.
        # Let's use a generally available one like 'gemini-1.5-flash-latest' or 'gemini-pro'.
        model = genai.GenerativeModel(model_name='gemini-1.5-flash-latest')
        
        # Craft a good prompt!
        prompt = (
            f"You are a friendly weather assistant. Based on this weather data string: "
            f"'{weather_data_str}', provide a short, engaging weather summary "
            f"(1-2 sentences) for the general public. Include one small, actionable "
            f"tip for the day (e.g., 'Don't forget your umbrella!' or 'Perfect day for a walk!')."
        )
        
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        app.logger.error(f"Error with Gemini API: {e}")
        # Check for specific Gemini API errors if the SDK provides them
        # For example, if e has a 'message' attribute:
        # return f"AI summary currently unavailable. Error: {getattr(e, 'message', str(e))}"
        return "Summary currently unavailable due to an error."

