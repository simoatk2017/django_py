from django.urls import path
from .views import sender, getEmployees , getEmployee  , getRepair
urlpatterns = [
    path('', sender, name='sender'),
    path('employees/', getEmployees, name='employees'),
    path('employees/<int:id>', getEmployee, name='employee'),
    path('repairs/<int:id>', getRepair, name='repairs'),
]
