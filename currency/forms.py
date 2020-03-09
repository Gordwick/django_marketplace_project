from django import forms
from .models import CurrencyExchangeModel


class ExchangeForm(forms.ModelForm):

    class Meta:
        model = CurrencyExchangeModel
        fields = ['value_exchanged', ]