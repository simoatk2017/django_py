from django import forms
from django.core.exceptions import ValidationError

'''
https://www.sitepoint.com/django-send-email/
https://stackoverflow.com/questions/12806771/django-modelform-validation

to dooooooooooooo
https://www.geeksforgeeks.org/python-form-validation-using-django/
'''

from .models import Contact


class ContactForm(forms.ModelForm):


    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'expiration_date': forms.DateInput(),
        }
        '''
         widgets = {
            'name': forms.ch(attrs={'name': 'pub'}),
            'authors': forms.SelectMultiple(attrs={'name': 'aut'}),
            'category': forms.SelectMultiple(attrs={'name': 'cat'}),
        }
        '''

    def clean(self):
        cleaned_data = super().clean()
        inquiry = cleaned_data.get("inquiry")
        message = cleaned_data.get("message")

        if message and inquiry:
            # Only do something if both fields are valid so far.
            if "sex" in message:
                raise ValidationError(
                    "Sex not alowed in subject.")

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg

        call
        super().clean()
        """

        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip().capitalize()
        from_email = cl_data.get('email')
        subject = cl_data.get('inquiry')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg

    def send(self):
        subject, msg = self.get_info()
        print('inside   ', subject)
        return subject, msg
