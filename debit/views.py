from django.shortcuts import render, redirect
from .models import data, credit
from django.contrib.auth.models import User
from .forms import debit_form, credit_form, category, delete_record
from account.models import userСategories
from account.models import Profile


def check_email_verify(user_id):
    return Profile.objects.filter(user_id=user_id).values()[0]['email_verify']


def v_debit(request):
    form_1 = debit_form()
    form_2 = category()
    form_3 = delete_record()
    if_verify = False
    if request.user.is_authenticated :
        user_id = User.objects.filter(
            username=f'{request.user}').values()[0]['id']
        if_verify = check_email_verify(user_id)
        categoryJSON = {}
        if userСategories.objects.filter(user_id=user_id).exists():
            categoryJSON = userСategories.objects.filter(
                user_id=user_id).values()[0]["category"]
            form_1.add_choices(categoryJSON['debit'].copy())
        if request.method == 'POST':
            if 'date' in request.POST:
                form_1 = debit_form(request.POST)
                if form_1.is_valid():
                    db_form = form_1.create_db_form(user_id, request)
                    data.record(form=db_form)
                    return redirect(to='http://127.0.0.1:8000/data/debit')
            elif 'category' in request.POST:
                form_2 = category(request.POST)
                if form_2.is_valid():
                    if not request.POST["category"] in categoryJSON['debit']:
                        categoryJSON['debit'].append(request.POST["category"])
                    userСategories.objects.filter(
                        user_id=user_id).update(category=categoryJSON)
                    return redirect(to='http://127.0.0.1:8000/data/debit')
            elif 'record_id' in request.POST:
                data.delete(request=request.POST)
                return redirect(to='http://127.0.0.1:8000/data/debit')
    records = data.objects.all().order_by('-id')
    return render(request, 'debit/debit.html', {'debit_form': form_1, 
                                                'category_form': form_2, 
                                                'delete_form': form_3, 
                                                'records': records,
                                                'verify': if_verify
                                                })


def v_credit(request):
    form_1 = credit_form()
    form_2 = category()
    form_3 = delete_record()
    if_verify = False
    if request.user.is_authenticated:
        user_id = User.objects.filter(
            username=f'{request.user}').values()[0]['id']
        if_verify = check_email_verify(user_id)
        categoryJSON = {}
        if userСategories.objects.filter(user_id=user_id).exists():
            categoryJSON = userСategories.objects.filter(
                user_id=user_id).values()[0]["category"]
            form_1.add_choices(categoryJSON['credit'].copy())
        if request.method == 'POST':
            if 'date' in request.POST:
                form_1 = credit_form(request.POST)
                if form_1.is_valid():
                    db_form = form_1.create_db_form(user_id, request)
                    credit.record(form=db_form)
                    return redirect(to='http://127.0.0.1:8000/data/credit')
            elif 'category' in request.POST:
                form_2 = category(request.POST)
                if form_2.is_valid():
                    if not request.POST["category"] in categoryJSON['credit']:
                        categoryJSON['credit'].append(request.POST["category"])
                    userСategories.objects.filter(
                        user_id=user_id).update(category=categoryJSON)
                    return redirect(to='http://127.0.0.1:8000/data/credit')
            elif 'record_id' in request.POST:
                credit.delete(request=request.POST)
                return redirect(to='http://127.0.0.1:8000/data/credit')
    records = credit.objects.all().order_by('-id')
    return render(request, 'debit/credit.html', {'debit_form': form_1, 
                                                 'category_form': form_2, 
                                                 'delete_form': form_3, 
                                                 'records': records,
                                                 'verify': if_verify
                                                 })
