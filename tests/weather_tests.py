import os
from services.weather_report import WeatherReportService

OWM_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

service = WeatherReportService(own_api_key=OWM_API_KEY)

# Ask the user for a city
city = input("Enter city (and optional country code, e.g., 'Paris, FR'): ")

try:
    # Fetch forecast
    forecast = service.get_owm_forecast(city)
    print(f"\nForecast JSON for {city} received successfully.\n")

    # Convert forecast to string for AI summary
    forecast_str = str(forecast)

    # Generate summary
    summary = service.get_gemini_summary(forecast_str)
    print("\nAI Weather Summary:\n")
    print(summary)

except Exception as e:
    print(f"Error: {e}")