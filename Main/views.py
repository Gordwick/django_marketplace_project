from django.shortcuts import render, redirect
from .forms import UserCurrencyOwnedForm, UserForm
from rest_framework.views import APIView
from django.http import HttpResponseBadRequest
from currency.models import CurrencyOwned
import traceback
from django.contrib.auth.models import User
from currency.serializers import UserSerializer


class MainPage(APIView):

    def get(self, request):
        return render(request, 'Main/main_page.html')


class RegistrationPage(APIView):

    def post(self, request):
        level_map = {1: {'EUR': 10000}, 2: {'GBP': 5000}, 3: {'PLN': 1000}}
        level = level_map[int(request.data['level'])]

        def validate_level(level):
            return True if int(level) in [1, 2, 3] else False

        registered = False

        try:
            print(request.data)
            user_serializer = UserSerializer(data=request.data)
            user_serializer.is_valid()# TODO: check if email already in the database
            user_object = user_serializer.save()
            # user_data = {
            #     'username': request.data['username'],
            #     'email': request.data['email'],
            #     'password': request.data['password']
            # }
            # user_object = UserForm(user_data)
            # user_object.is_valid()
            # user_object = user_object.save()
            if validate_level(request.data['level']):
                currency = CurrencyOwned(user=user_object, **level)
                currency.save()
            else:
                raise Exception('Wrong level set')

        except Exception as e:  # TODo : create actual page
            print(traceback.format_exc())
            return HttpResponseBadRequest()

        return render(request, 'registration/register.html', {'registered': registered})

    def get(self, request):
        user_form = UserForm()

        return render(request, 'registration/register.html', {'registered': False,
                                                              'user_form': user_form
                                                              })
