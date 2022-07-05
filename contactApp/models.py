from django.db import models
import datetime


# Create your models here.
def expire():
    return datetime.datetime.today() + datetime.timedelta(days=15)


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    inquiry = models.CharField(max_length=70)
    message = models.TextField()
    date = models.DateField()
    expiration_date = models.DateField(default=datetime.date.today)
    CHOICES = (
        ('Debt', (
            (11, 'Credit Card'),
            (12, 'Student Loans'),
            (13, 'Taxes'),
        )),
        ('Entertainment', (
            (21, 'Books'),
            (22, 'Games'),
        )),
        ('Everyday', (
            (31, 'Groceries'),
            (32, 'Restaurants'),
        )),
    )
    category = models.CharField(max_length=80, choices=CHOICES)

    # date = models.DateField(widget=forms.SelectDateWidget)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    salary = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=100)
    year = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=3)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.model


class Repair(models.Model):
    company = models.CharField(max_length=100)
    description_of_repairation = models.TextField()
    price_repair = models.DecimalField(max_digits=8, decimal_places=3)
    date_repair = models.DateTimeField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.company

