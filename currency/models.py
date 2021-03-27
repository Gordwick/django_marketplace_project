from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal


class CurrencyExchangeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # additional
    date = models.DateField()
    exchanged_currency = models.CharField(max_length=3)
    value_exchanged = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal(0.1))])
    acquired_currency = models.CharField(max_length=3)
    exchange_rate = models.DecimalField(max_digits=12, decimal_places=2)
    value2_acquired = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return "" + self.user.username + "  " + str(self.date) + ""


class CurrencyOwned(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional fields

    GBP = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    HKD = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    IDR = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    ILS = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    DKK = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    INR = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    CHF = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    MXN = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    CZK = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    SGD = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    THB = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    HRK = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    EUR = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    MYR = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    NOK = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    CNY = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    BGN = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    PHP = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    PLN = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    ZAR = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    CAD = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    ISK = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    BRL = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    RON = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    NZD = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    TRY = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    JPY = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    RUB = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    KRW = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    USD = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    AUD = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    HUF = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    SEK = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.user.username