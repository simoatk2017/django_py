from django.shortcuts import render
from django.views.generic import TemplateView
import datetime


# Create your views here.
class HomeView(TemplateView):
    template_name = 'smartnotes/smartnotes.html'
    extra_context = {'date': datetime.date.today()}
