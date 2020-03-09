from django import forms
from django.contrib.auth.models import User
from currency.models import Currency_owned


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class User_Currency_owned_Form(forms.ModelForm):

    class Meta():
        model = Currency_owned
        exclude =('user',)