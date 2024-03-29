from django.db import models

'''
https://www.geeksforgeeks.org/django-form-field-custom-widgets/
'''
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=300)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()


    def __str__(self):
        return self.subject
