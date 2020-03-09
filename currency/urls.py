from django.urls import path, include
from .views import display_for_currency, display_all_currencies, currency_exchange#, ajax_first_try

urlpatterns = [
    path('', display_all_currencies, name="display_all_currencies"),
    path('view/<str:name>/', display_for_currency, name="display_for_currency"),
    path('exchange/<str:owned>/<str:needed>/', currency_exchange, name="currency_exchange"),
]
