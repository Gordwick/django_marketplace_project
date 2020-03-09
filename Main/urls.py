from django.contrib import admin
from django.urls import path, include
from .views import main_page
from .views import registration_page


urlpatterns = [
    path('', main_page, name='main_page'),
    path('currency/', include('currency.urls')),
    path('register/', registration_page, name='register'),
]
