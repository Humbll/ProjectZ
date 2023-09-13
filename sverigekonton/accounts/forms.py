from django import forms
from .models import Account

class AccountRegistrationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }