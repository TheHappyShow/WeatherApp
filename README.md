🌤 Weather API Wrapper Service
📌 Описание

Этот сервис предоставляет REST API для получения данных о погоде по коду города.

Использует внешний сервис OpenWeather API (или другой погодный API).

Реализует кэширование в Redis для уменьшения количества запросов к внешнему API.

Сервис построен на Django REST Framework.

🚀 Возможности

Получение текущей погоды по городу.

Автоматическое кэширование ответа в Redis (время жизни — 12 часов).

Если данные есть в кэше — возвращаются они, если устарели — идёт запрос к внешнему API.

Swagger-документация API.

🛠 Технологии

Python 3.10+

Django 4+ / DRF

Redis (как in-memory cache)

drf_yasg (Swagger/Redoc документация)

django-cors-headers (CORS поддержка)

⚙️ Установка и запуск
1. Клонирование репозитория
git clone https://github.com/username/weather-api-wrapper.git
cd weather-api-wrapper

2. Создание виртуального окружения
python -m venv venv
source venv/bin/activate   # для Linux/Mac
venv\Scripts\activate      # для Windows

3. Установка зависимостей
pip install -r requirements.txt

4. Настройка переменных окружения
Создайте файл .env и укажите:
DEBUG=True
SECRET_KEY=your_secret_key

# API ключ для OpenWeather
OPENWEATHER_API_KEY=your_api_key_here

# Настройки Redis
REDIS_HOST=localhost
REDIS_PORT=6379

5. Запуск Redis
Для локального запуска:
docker run -d -p 6379:6379 redis

6. Запуск сервиса
python manage.py migrate
python manage.py runserver

📡 Примеры API запросов
Получить погоду по городу
GET /api/weather/?city=Tashkent

Пример ответа:
{"coord":{"lon":66.9597,"lat":39.6542},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"base":"stations","main":{"temp":34.68,"feels_like":32.41,"temp_min":34.68,"temp_max":34.68,"pressure":1006,"humidity":17,"sea_level":1006,"grnd_level":917},"visibility":10000,"wind":{"speed":2.06,"deg":360},"clouds":{"all":0},"dt":1756370223,"sys":{"type":1,"id":9013,"country":"UZ","sunrise":1756342596,"sunset":1756390243},"timezone":18000,"id":1216265,"name":"Samarkand","cod":200}

📖 Документация API
После запуска проекта доступна по адресам:

Swagger UI → http://127.0.0.1:8000/swagger/

Redoc → http://127.0.0.1:8000/redoc/

📌 TODO / Roadmap

