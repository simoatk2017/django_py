from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

'''
@login_required
def home(request):
    return render(request, "registration/success.html", {})





'''
# Views

def register(request):
    print('logiuiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return redirect('login')
    else:
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})
