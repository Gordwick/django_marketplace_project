from django import forms
from django.contrib.auth.models import User
from currency.models import CurrencyOwned


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserCurrencyOwnedForm(forms.ModelForm):

    class Meta:
        model = CurrencyOwned
        exclude =('user',)