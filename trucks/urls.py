# myapp/urls.py
from django.urls import path
from .views import find_foodtrucks

urlpatterns = [
    path('', find_foodtrucks, name='find_foodtrucks'),
]
