from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import MealSerialzer, RatingSerializer
from .models import Meal, Rating

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerialzer
    # Extra actions
    @action(methods={'post'}, detail=True)
    def rate_meal(self, request, pk=None):
        if 'rate' in request.data:
            """Create or Update"""
            meal = Meal.objects.get(pk=pk)
            username = request.data['username']
            user = User.objects.get(username=username)
            rate = request.data['rate']
            try:
                # update
                rating = Rating.objects.get(user=user.id, meal=meal.id)
                rating.rate = rate
                rating.save()

                serializer = RatingSerializer(rating, many=False)

                json = {
                    'message': 'Rate updated',
                    'result': serializer.data
                }
                return Response(json, status=status.HTTP_202_ACCEPTED)
            except:
                # create
                rating = Rating.objects.create(user=user, meal=meal, rate=rate)
                rating.save()
                
                serializer = RatingSerializer(rating, many=False)

                json = {
                    'message': 'Rate created',
                    'result': serializer.data
                }
                return Response(json, status=status.HTTP_201_CREATED)
        else:
            json = {
                'message': 'rating error! starts not provided!'
            }
            return Response(json, status=status.HTTP_400_BAD_REQUEST)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer