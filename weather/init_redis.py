import redis, json
import subprocess
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

# Запуск Redis (только для pet-проекта, не для продакшена!)
subprocess.Popen(["redis-server"])

redis_host = config("REDIS_HOST")
redis_port = config("REDIS_PORT")
# Подключение к Redis
r = redis.Redis(host=f"{redis_host}", port=int(redis_port), decode_responses=True)

data = weather_api('Tashkent') # Для примера только один город
# сохраняем JSON целиком на 12 час
r.setex("weather:Tashkent", 43200, json.dumps(data))
