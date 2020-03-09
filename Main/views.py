from django.shortcuts import render, redirect
from .forms import User_Currency_owned_Form,UserForm


def main_page(request):
    return render(request, 'Main/main_page.html')


def registration_page(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        currency_form = User_Currency_owned_Form(data=request.POST)

        if user_form.is_valid() and currency_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)     #hashing password
            user.save()

            currency = currency_form.save(commit=False)
            currency.user = user
            currency.save()
            registered = True
        else:
            print(user_form.errors, currency_form.error_class)
    else:
        user_form = UserForm()
        currency_form = User_Currency_owned_Form()

    return render(request, 'registration/register.html', {'registered': registered,
                                                          'user_form': user_form,
                                                          'currency_form': currency_form})