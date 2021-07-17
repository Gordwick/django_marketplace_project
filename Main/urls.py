from django.contrib import admin
from django.urls import path, include
from .views import MainPage
from .views import RegistrationPage



urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('currency/', include('currency.urls')),
    path('register/', RegistrationPage.as_view(), name='register'),  # TODO: registration does not work
]
