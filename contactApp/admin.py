from django.contrib import admin

# Register your models here.
from .models import Employee, Car, Repair

admin.site.register(Employee)
admin.site.register(Car)
admin.site.register(Repair)
