from django.shortcuts import render
from django.views.generic import TemplateView
import json
from account.models import userСategories
from django.contrib.auth.models import User
from debit.models import data, credit
from datetime import datetime


# Create your views here.
def month(request):
    # period = 31 days
    if request.user.is_authenticated:
        user_id = User.objects.filter(
            username=f'{request.user}').values()[0]['id']
        categoryJSON = {}
        if userСategories.objects.filter(user_id=user_id).exists():
            categoryJSON = userСategories.objects.filter(
                user_id=user_id).values()[0]["category"]
            all_debit_records = data.objects.filter(user_id=user_id).all()
            all_credit_records = credit.objects.filter(user_id=user_id).all()
    debit_dict = make_out_data_month(all_debit_records)
    credit_dict = make_out_data_month(all_credit_records)
    median_credit = solve_median(credit_dict['amount'])
    median_debit = solve_median(debit_dict['amount'])
    debit_hist = make_histogram(all_debit_records)
    credit_hist = make_histogram(all_credit_records)
    print(debit_dict)
    make_out_data_week(all_debit_records)
    out_data = {"debit_dict": debit_dict,
                "credit_dict": credit_dict,
                "median_credit": median_credit,
                "median_debit": median_debit,
                "hist_debit": debit_hist,
                "hist_credit": credit_hist
                }
    return render(request, 'user_stat/script.html', out_data)

def week(request):
    # period = 31 days
    if request.user.is_authenticated:
        user_id = User.objects.filter(
            username=f'{request.user}').values()[0]['id']
        categoryJSON = {}
        if userСategories.objects.filter(user_id=user_id).exists():
            categoryJSON = userСategories.objects.filter(
                user_id=user_id).values()[0]["category"]
            all_debit_records = data.objects.filter(user_id=user_id).all()
            all_credit_records = credit.objects.filter(user_id=user_id).all()
    debit_dict = make_out_data_week(all_debit_records)
    credit_dict = make_out_data_week(all_credit_records)
    median_credit = solve_median(credit_dict['amount'])
    median_debit = solve_median(debit_dict['amount'])
    debit_hist = make_histogram(all_debit_records)
    credit_hist = make_histogram(all_credit_records)
    out_data = {"debit_dict": debit_dict,
                "credit_dict": credit_dict,
                "median_credit": median_credit,
                "median_debit": median_debit,
                "hist_debit": debit_hist,
                "hist_credit": credit_hist
                }
    return render(request, 'user_stat/script.html', out_data)


def solve_median(list_of_amounts):
    median = 0
    for i in list_of_amounts:
        median += i
    median /= len(list_of_amounts)
    return round(median, 2)

def make_out_data_week(records):
    list_of_records_per_mounth = {'period': [],
                                  'amount': []
                                  }
    weeks_list = {}
    for i in range(53):
        list_of_records_per_mounth['amount'].append(0)
        list_of_records_per_mounth['period'].append(i)
    for el in records:
        for i in range(53):
            date = str(el.date)
            year = int(date[0:4])
            month = int(date[5:7])
            day = int(date[8:10])
            week_number = int(datetime.date(datetime(year, month, day)).isocalendar()[1])
            if week_number == i:
                list_of_records_per_mounth['amount'][i] += float(round(el.amount))
    return list_of_records_per_mounth

def make_out_data_month(records):
    list_of_records_per_mounth = {'period': [],
                                  'amount': []
                                  }
    month = ['01', '02', '03', '04', '05', '06',
             '07', '08', '09', '10', '11', '12']
    list_of_records_per_mounth['period'] = month.copy()
    for i in month:
        summ = 0
        for el in records:
            if str(el.date)[0:4] == '2023' and str(el.date)[5:7] == i:
                print(el.date)
                summ += float(el.amount)
        list_of_records_per_mounth['amount'].append(round(summ))
    return list_of_records_per_mounth.copy()


def make_histogram(records):
    list_of_records_per_mounth = {'category' : [],
                                  'amount' : []}
    for el in records:
        if not el.category in list_of_records_per_mounth['category']:
            list_of_records_per_mounth['category'].append(el.category)
            list_of_records_per_mounth['amount'].append(0)
    summ_of_enother = 0
    summ = 0
    for el in records:
        summ += float(el.amount)
    for i in range(len(list_of_records_per_mounth['category'])):
        category_amount = 0
        for el in records:
            if el.category == list_of_records_per_mounth['category'][i]:
                category_amount += float(el.amount)
        if category_amount / summ > 0.01:
            list_of_records_per_mounth['amount'][i] = round(category_amount)
        else:
            list_of_records_per_mounth['amount'][i] = 0
            summ_of_enother += float(el.amount)
    if not 'другое' in list_of_records_per_mounth['category']:
        list_of_records_per_mounth['category'].append('другое')
        list_of_records_per_mounth['amount'].append(round(summ_of_enother))
    for i in range(len(list_of_records_per_mounth['amount'])):
        if list_of_records_per_mounth['amount'][i - 1] == 0:
            print(list_of_records_per_mounth['category'].pop(i - 1))
            print(list_of_records_per_mounth['amount'].pop(i - 1))
    return list_of_records_per_mounth.copy()
