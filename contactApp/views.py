from django.shortcuts import render
from .forms import ContactForm
from .models import Employee, Car, Repair
from datetime import date
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


# Create your views here.


def sender(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            subject, msg = form.send()
            print(msg)
            return render(request, 'contactApp/success.html', {
                'subject': subject,
                'msg': msg
            })
    return render(request, 'contactApp/sender_email.html', {'form': form})


def getEmployees(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees,
        'today': date.today()
    }
    return render(request, 'contactApp/employee.html', context)


def getEmployee(request, id):
    employee = Employee.objects.get(pk=id)
    cars = employee.car_set.all()

    context = {
        'employee': employee,
        'today': date.today(),
        'cars': cars,

    }
    return render(request, 'contactApp/employee_detail.html', context)


def getRepair(request, id):
    car = get_object_or_404(Car, pk=id)
    # car = Car.objects.get(pk=id)
    repairs = car.repair_set.all()
    total = 0
    for t in repairs:
        total += t.price_repair
    context = {

        'today': date.today(),
        'car': car,
        'repairs': repairs,
        'total': total
    }
    return render(request, 'contactApp/repairs_list.html', context)
