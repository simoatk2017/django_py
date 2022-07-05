from django.urls import path
from .views import contact_me
urlpatterns = [
    path('', contact_me, name='contact.contact'),
]
