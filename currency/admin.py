from django.contrib import admin
from .models import CurrencyOwned, CurrencyExchangeModel
# Register your models here.

admin.site.register(CurrencyOwned)
admin.site.register(CurrencyExchangeModel)