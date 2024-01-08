from django.contrib import admin
from django.urls import path,include
from .views import weather
from . import views
urlpatterns = [
    path('',views.weather,name='weather')
]