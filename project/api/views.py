from rest_framework import viewsets
from django.shortcuts import render
from .serializers import MealSerialzer, RatingSerializer
from .models import Meal, Rating

# Create your views here.

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerialzer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer