import json
from django.shortcuts import render
import redis
from .serializers import WeatherSerializer
from .utils import weather_api
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


r = redis.Redis(host='localhost', port=6379, db=0)


@api_view(['GET'])
def weather_list(request):
    # берём данные из query-параметров
    serializer = WeatherSerializer(data=request.query_params)

    if serializer.is_valid():
        city = serializer.validated_data['city']

        # Проверяем кэш
        city_data = r.get(f"weather:{city}")
        if city_data is None:
            city_data = weather_api(city)
            if "error" not in city_data:  # если API вернул нормальный результат
                r.setex(f"weather:{city}", 43200, json.dumps(city_data))
        else:
            city_data = json.loads(city_data)

        return Response(city_data)

    return Response(serializer.errors, status=400)