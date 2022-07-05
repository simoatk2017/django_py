from django.shortcuts import render
from .forms import RegistrationForm


# Create your views here.

def registration(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        '''
        'firstName':request.POST.get('firstName'),
          'lastName': request.POST.get('lastName'),
          'age': request.POST.get('age'),
        '''
        if form.is_valid():
            context = {


            }
            print(form.cleaned_data)
            context['form'] = form
            context['firstName'] = form.cleaned_data.get('firstName')
            context['lastName'] = form.cleaned_data.get('lastName')
            context['age'] = form.cleaned_data.get('age')
            context['email'] = form.cleaned_data.get('email')
            context['gender'] = form.cleaned_data.get('gender')

            return render(request, 'formApp/postdata.html', context)
        else:
            return render(request, 'formApp/postdata.html',{'form':form})

    return render(request, 'formApp/postdata.html', {

        'form': form
    })
