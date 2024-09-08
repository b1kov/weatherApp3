import sys
import time  # Import time to add delays between iterations
import requests
from datetime import datetime


def get_weather(api_key, city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}"
    response = requests.get(url)
    return response.json()


def get_forecast(api_key, city_name, date):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&units=metric&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    forecast = None
    for item in data["list"]:
        if item["dt_txt"].startswith(date):
            forecast = item
            break
    return forecast


if __name__ == "__main__":
    api_key = "ae518f91b64260f7014bb89de301f5a0"  # Replace with your actual API key

    # Check if command-line arguments are provided
    if len(sys.argv) == 3:
        city_name = sys.argv[1]
        future_date = sys.argv[2]
    else:
        # Prompt the user for input
        city_name = input("Enter city name: ")
        future_date = input("Enter future date (YYYY-MM-DD): ")

    while True:  # Start an infinite loop to keep the script running
        current_weather = get_weather(api_key, city_name)
        future_weather = get_forecast(api_key, city_name, future_date)

        print(
            f"Current temperature in {city_name}: {current_weather['main']['temp']}°C, {current_weather['weather'][0]['description']}"
        )
        if future_weather:
            print(
                f"Temperature in {city_name} on {future_date}: {future_weather['main']['temp']}°C, {future_weather['weather'][0]['description']}"
            )
        else:
            print("No forecast available for the specified date.")

        time.sleep(60)  # Wait for 60 seconds before repeating the loop
