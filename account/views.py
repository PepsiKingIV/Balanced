from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from . import forms
from .models import userСategories
import secrets




def user_login(request):
    data = ''
    if request.method == 'POST':
        token = secrets.token_urlsafe()
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    user_id = User.objects.filter(username=f'{request.user}').values()[0]['id']
                    if not userСategories.objects.filter(user_id=user_id).exists():
                        u = userСategories.objects.create(user_id=user_id, telegram_id='tel_id', category = {'debit': [], 'credit':[]})
                    data = 'Успешно'
                else:
                    data = 'Несуществующий аккаунт'
            else:
                data = 'Неверный логи либо пароль'
            form = LoginForm()
    else:
        form = LoginForm()
        try:
            token = User.objects.filter(username=f'{request.user}').values()[0]['first_name']
        except:
            token = 'none'
    return render(request, 'account/login.html', {'form': form, 'data': data, 'token': token})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        token = secrets.token_urlsafe()
        print(token)
        if user_form.is_valid():
            username = user_form.data['username']
            email = user_form.data['email']
            if User.objects.filter(username=username).exists():
                return render(request, 'account/registr.html', {'user_form': user_form, 'data': 'Пользователь с таким именем уже существует'})
            elif User.objects.filter(email=email):
                return render(request, 'account/registr.html', {'user_form': user_form, 'data': 'Пользователь с такой почтой уже существует'})
            else:
                new_user = user_form.save(commit=False)
                new_user.first_name = token
                new_user.set_password(user_form.cleaned_data['password'])
                new_user.save()
                return render(request, 'account/registr.html', {'user_form': user_form, 'data': 'Регистрация прошла успешно'})
        else:
            return render(request, 'account/registr.html', {'user_form': user_form, 'data': 'Пользователь с таким именем уже существует'})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/registr.html', {'user_form': user_form })


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
    
def new_token(request):
    token = secrets.token_urlsafe()
    old_token = User.objects.filter(username=f'{request.user}').values()[0]['first_name']
    User.objects.filter(first_name=old_token).update(first_name=token)
    return redirect(to='http://127.0.0.1:8000/account/login/')


#чтобы ограничить количество писем в минуту можно сделать асихронную функцию, которая будет ждать какое-то время и после разрешать повторную отправку