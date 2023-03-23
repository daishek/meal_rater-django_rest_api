from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import RatingViewSet, MealViewSet, UserViewSet
from rest_framework.authtoken.views import obtain_auth_token
router = routers.DefaultRouter()
router.register('meals', MealViewSet)
router.register('rating', RatingViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tokenrequest/', obtain_auth_token)
]