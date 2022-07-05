from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm

'''
https://www.javatpoint.com/django-usercreationform

'''
# Create your views here.

def register(request):
    print('registerrrrrrrrrrrrrrrrrrrr')
    if request.POST == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return  redirect('login')
    else:
        form = UserCreationForm()


    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)