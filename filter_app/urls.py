from django.urls import path
from . import views

urlpatterns = [
    path('', views.filter_example_1, name='filter_example_1'),
]
