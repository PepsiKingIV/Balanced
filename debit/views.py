from django.shortcuts import render
from .models import debit, credit
from django.contrib.auth.models import User
from .forms import debit_form, credit_form


from account.models import userСategories


def v_debit(request):
    msg = 'Данные записаны'
    user_id = User.objects.filter(
        username=f'{request.user}').values()[0]['id']
    if debit.objects.filter(user_id=user_id).exists():
        debitTableRecords = debit.objects.filter(user_id=user_id)
        if userСategories.objects.filter(user_id=user_id).exists():
            categoryRecords = userСategories.objects.filter(user_id=user_id)
    categoryRecords = False
    debitTableRecords = False
    if request.method == 'POST':
        form = debit_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            msg = 'Форма заполнена неверно'

    else:
        form = debit_form()
    data = {"categoryRecords": categoryRecords,
                "debitTableRecords": debitTableRecords,
                "msg": msg,
                "form": form
                }
    return render(request, 'debit/debit.html', data)


def v_credit(request):
    user_id = User.objects.filter(username=f'{request.user}').values()[0]['id']
    if credit.objects.filter(user_id=user_id).exists():
        creditTableRecords = debit.objects.filter(user_id=user_id)
        if userСategories.objects.filter(user_id=user_id).exists():
            categoryRecords = userСategories.objects.filter(user_id=user_id)
        else:
            categoryRecords = False
        data = {"categoryRecords": categoryRecords,
                "creditTableRecords": creditTableRecords
                }
        return render(request, 'debit/credit.html', data)
    return render(request, 'debit/credit.html')
