from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from . import forms



def user_login(request):
    data = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd['username'])
            print(cd['password'])
            user = authenticate(
                username=cd['username'], password=cd['password'])
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    data = 'Успешно'
                else:
                    data = 'Несуществующий аккаунт'
            else:
                data = 'Неверный логи либо пароль'
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form, 'data': data})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            username = user_form.data['username']
            email = user_form.data['email']
            if User.objects.filter(username=username).exists():
                return render(request, 'account/registr.html', {'user_form': user_form, 'data': 'Пользователь с таким именем уже существует'})
            elif User.objects.filter(email=email):
                return render(request, 'account/registr.html', {'user_form': user_form, 'data': 'Пользователь с такой почтой уже существует'})
            else:
                new_user = user_form.save(commit=False)
                new_user.set_password(user_form.cleaned_data['password'])
                new_user.save()
                return render(request, 'account/registr.html', {'user_form': user_form, 'data': 'Регистрация прошла успешно'})
        else:
            return render(request, 'account/registr.html', {'user_form': user_form, 'data': 'Пользователь с таким именем уже существует'})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/registr.html', {'user_form': user_form})


def logout_view(request):
    logout(request)
    return redirect(to='http://127.0.0.1:8000/account/login/')


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


class PasswordResetView2(PasswordResetView):
    form_class = forms.PasswordResetForm2

class PasswordResetConfirmView2(PasswordResetConfirmView):
    form_class = forms.SetPasswordForm2