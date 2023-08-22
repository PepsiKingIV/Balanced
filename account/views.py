from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    data = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd['username'])
            print(cd['password'])
            user = authenticate(username=cd['username'], password=cd['password'])
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    data = 'Успешно'
                else:
                    data = 'Несуществующий аккаунт'
            else:
                data = 'Произошла ошибка регистрации'
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form, 'data': data})