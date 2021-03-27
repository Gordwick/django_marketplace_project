from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from forex_python.converter import CurrencyRates
from forex_python.converter import get_rate
from datetime import datetime, timedelta
from .models import CurrencyOwned, CurrencyExchangeModel
from .forms import ExchangeForm
from django.http import HttpResponse
import decimal as d
from django.db import connection
from django.http import Http404


def display_for_currency(request, name="USD"):
    c = CurrencyRates()
    c = c.get_rates(name)
    return render(request, 'currency/currency.html', {'currency': name, 'rates': c})


@login_required
def display_all_currencies(request):  # TODO: what if none owned money - investigate if error
    c = CurrencyRates()
    c = c.get_rates('USD')
    l = []
    for el, el2 in c.items():
        l.append(el)
    users_data = list(CurrencyOwned.objects.values().filter(user=request.user))
    owned_currency = users_data[0]
    owned_currency.pop('id')
    owned_currency.pop('user_id')
    return render(request, 'currency/currencies_main.html', {'owned_currency': owned_currency})


@login_required
def currency_exchange(request, owned, needed):
    datetime_object = datetime.now()
    datetime_week_old = datetime_object - timedelta(days=7)
    now = get_rate(owned, needed, datetime_object)
    then = get_rate(owned, needed, datetime_week_old)

    percentage = int((now - then) * 10000) / 100

    if request.method == "POST":
        exchange_form = ExchangeForm(data=request.POST)
        if exchange_form.is_valid():
            # saving transaction
            fee = d.Decimal("0.96")
            obj = CurrencyExchangeModel()
            obj.value_exchanged = exchange_form.cleaned_data['value_exchanged']
            obj.exchanged_currency = owned
            obj.acquired_currency = needed
            obj.date = datetime.now()
            obj.exchange_rate = round(get_rate(owned, needed, datetime.now()), 2)
            obj.value2_acquired = round(
                fee * exchange_form.cleaned_data['value_exchanged'] * d.Decimal(obj.exchange_rate), 2)
            obj.user = request.user
            obj.save()

            # exchange

            usr = get_object_or_404(CurrencyOwned, user=request.user)
            owned_client = 'SELECT c."{}" FROM currency_currency_owned as c WHERE user_id={};'.format(
                obj.exchanged_currency, usr.user_id)
            needed_client = 'SELECT c."{}" FROM currency_currency_owned as c WHERE user_id={};'.format(
                obj.acquired_currency, usr.user_id)
            with connection.cursor() as cursor:
                cursor.execute(owned_client)
                owned_client = cursor.fetchone()
                cursor.execute(needed_client)
                needed_client = cursor.fetchone()
                owned_client = d.Decimal(round(owned_client[0], 2))
                needed_client = d.Decimal(round(needed_client[0], 2))
            if owned_client > obj.value_exchanged:
                giving = 'UPDATE currency_currency_owned SET "{}"={} WHERE user_id={};'.format(obj.exchanged_currency,
                                                                                               owned_client - obj.value_exchanged,
                                                                                               usr.user_id)
                getting = 'UPDATE currency_currency_owned SET "{}"={} WHERE user_id={};'.format(obj.acquired_currency,
                                                                                                needed_client + obj.value2_acquired,
                                                                                                usr.user_id)
                try:
                    with connection.cursor() as cursor:
                        cursor.execute(giving)
                        cursor.execute(getting)
                        registered = True
                except(Exception):
                    return HttpResponse('<h1>Databese connection lost</h1>')
            else:
                return HttpResponse('<h1>Form not valid - in construction ...</h1>')

        else:
            print(exchange_form.error_class)

        return redirect('main_page')
    context = {'exchange_form': ExchangeForm(),
               'owned': owned,
               'needed': needed,
               'percentage': percentage,
               }
    return render(request, 'currency/exchange_panel.html', context)
