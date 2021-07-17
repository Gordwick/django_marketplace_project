from django.shortcuts import render, redirect
from .forms import UserCurrencyOwnedForm, UserForm
from django.contrib.auth.models import User
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
        user_object = None
        try:
            print(request.data)
            user_serializer = UserSerializer(data={'username': request.data['username'],
                                                   'email': request.data['email'],
                                                   'password': request.data['password']})

            if user_serializer.is_valid():
                user_object = User.objects.create_user(**user_serializer.data)
                user_object.save()
                # TODO: check if email already in the database
                if validate_level(request.data['level']):
                    currency = CurrencyOwned(user=user_object, **level)
                    currency.save()
                else:
                    raise Exception('Wrong level set')
                registered = True
            else:
                raise Exception('Input not valid')

        except Exception as e:  # TODo : create actual page

            if user_object:
                user_object.delete()

            print(traceback.format_exc())  # TODO: create logger
            return HttpResponseBadRequest()

        return render(request, 'registration/register.html', {'registered': registered})

    def get(self, request):
        user_form = UserForm()

        return render(request, 'registration/register.html', {'registered': False,
                                                              'user_form': user_form
                                                              })
