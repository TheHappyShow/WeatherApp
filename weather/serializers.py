from rest_framework import serializers
import re

class WeatherSerializer(serializers.Serializer):
    city = serializers.CharField()

    def validate_city(self, word: str) -> str:
        cleaned_word = word.strip()
       # if cleaned_word.isalpha():  - Проблема – города типа New York или São Paulo не пройдут проверку.
        if re.match(r"^[a-zA-Z\s\-]+$", cleaned_word):
            return cleaned_word
        else:
            raise serializers.ValidationError('Неверный формат города')
