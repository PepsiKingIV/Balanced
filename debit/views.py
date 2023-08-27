from django.shortcuts import render, redirect
from .models import data, credit
from django.contrib.auth.models import User
from .forms import debit_form, credit_form, category, delete_record
from account.models import userСategories


from account.models import userСategories


def v_debit(request):
    form_1 = debit_form()
    form_2 = category()
    form_3 = delete_record()
    if request.user.is_authenticated:
        user_id = User.objects.filter(username=f'{request.user}').values()[0]['id']
        categoryJSON = {}
        if userСategories.objects.filter(user_id=user_id).exists():
            categoryJSON = userСategories.objects.filter(
                user_id=user_id).values()[0]["category"]
            choices = []
            categories = categoryJSON['debit'].copy()
            for i in categories:
                choices.append([i, i])
            form_1.base_fields['category'].choices = choices
        if request.method == 'POST':
            if 'date' in request.POST:
                form_1 = debit_form(request.POST)
                print(request.POST)
                print(form_1)
                if form_1.is_valid():
                    print("done")
                    data.objects.create(user_id=user_id, date=request.POST['date'],
                                        category=request.POST['category'], amount=request.POST['amount'])
                    return redirect(to='http://127.0.0.1:8000/data/debit')
            elif 'category' in request.POST:
                form_2 = category(request.POST)
                if form_2.is_valid():
                    if not request.POST["category"] in categoryJSON['debit']:
                        categoryJSON['debit'].append(request.POST["category"])
                    if 'cat_d' in categoryJSON["debit"]:
                        categoryJSON["debit"].remove('cat_d')
                    print(categoryJSON)
                    userСategories.objects.filter(
                        user_id=user_id).update(category=categoryJSON)
                    categoryJSON.clear()
                    return redirect(to='http://127.0.0.1:8000/data/debit')
        else:
            records = data.objects.all()
    else:
        records = 'none'
    return render(request, 'debit/debit.html', {'debit_form': form_1, 'category_form': form_2, 'records': records})


def v_credit(request):
    form_1 = credit_form()
    form_2 = category()
    form_3 = delete_record()
    if request.user.is_authenticated:
        user_id = User.objects.filter(username=f'{request.user}').values()[0]['id']

        categoryJSON = {}
        if userСategories.objects.filter(user_id=user_id).exists():
            categoryJSON = userСategories.objects.filter(
                user_id=user_id).values()[0]["category"]
            choices = []
            categories = categoryJSON['credit'].copy()
            for i in categories:
                choices.append([i, i])
            form_1.base_fields['category'].choices = choices
        print("0")
        if request.method == 'POST':
            if 'date' in request.POST:
                form_1 = debit_form(request.POST)
                print(request.POST)
                print(form_1)
                if form_1.is_valid():
                    print("done")
                    credit.objects.create(user_id=user_id, date=request.POST['date'],
                                        category=request.POST['category'], 
                                        amount=request.POST['amount'], 
                                        priority = request.POST['priority'])
                    return redirect(to='http://127.0.0.1:8000/data/credit')
            elif 'category' in request.POST:
                form_2 = category(request.POST)
                if form_2.is_valid():
                    if not request.POST["category"] in categoryJSON['credit']:
                        categoryJSON['credit'].append(request.POST["category"])
                    if 'cat_c' in categoryJSON["credit"]:
                        categoryJSON["credit"].remove('cat_c')
                    print(categoryJSON)
                    userСategories.objects.filter(
                        user_id=user_id).update(category=categoryJSON)
                    categoryJSON.clear()
                    return redirect(to='http://127.0.0.1:8000/data/credit')
        else:
            records = credit.objects.all()
    else: 
        records = ''

    return render(request, 'debit/credit.html', {'debit_form': form_1, 'category_form': form_2, 'records': records})
