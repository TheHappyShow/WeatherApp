import requests
from decouple import config


def weather_api(city:str) -> dict:
    api_key = config("WEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url).json()

    if response.get('cod') != 200:
        return {"error": "City not found"}

    else:
        return response


