from rest_framework import serializers
from .models import Meal, Rating


class MealSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'title', 'description']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'rate', 'meal', 'user']