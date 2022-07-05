from django import forms


class RegistrationForm(forms.Form):
    GENDER = (('male', 'MALE'), ('femele', 'FEMELE'))

    firstName = forms.CharField(widget=forms.Textarea, required=False)
    lastName = forms.CharField(max_length=50)
    age = forms.IntegerField()
    email = forms.EmailField()
    gender = forms.CharField(widget=forms.Select(choices=GENDER))
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
       cleaned_data = super().clean()
       f_name = cleaned_data.get('firstName')
       if len(f_name) < 5:
            raise forms.ValidationError('FirstName Minimum 6 characters long should be.')


    """
    def clean_firstName(self):
        first_name = self.cleaned_data.get('firstName')
        if len(first_name) > 15:
            raise forms.ValidationError('Pass should minimum 6 Characters long')
        return first_name

    def clean_password(self):
        password_input = self.cleaned_data.get('password')
        if len(password_input) < 10:
            raise forms.ValidationError('Weak password ,do not type coment passwords, please type strong password')
        return password_input

    def clear_email(self):
        email = self.cleaned_data.get('email')
        if email.find('@') == -1:
            print('starttttttttttttt')
            raise forms.ValidationError('Invalid email.')
        return email
    """