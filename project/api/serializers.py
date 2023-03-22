from rest_framework import serializers
from .models import Meal, Rating


class MealSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'title', 'description', 'avg_rating', 'no_of_ratings', 'get_avg']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'rate', 'meal', 'user']