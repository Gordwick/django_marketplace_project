from django.contrib import admin
from django.urls import path, include
from .views import MainPage
from .views import RegistrationPage
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage


urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('currency/', include('currency.urls')),
    path('register/', RegistrationPage.as_view(), name='register'),
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
]
