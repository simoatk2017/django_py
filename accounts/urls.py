from django.urls import path
from django.contrib import admin
from .views import register

urlpatterns = [
    path('', register, name='register')
]
