from django.shortcuts import render
from django.views.generic import TemplateView
import json
from account.models import userСategories
from django.contrib.auth.models import User
from debit.models import data, credit
from datetime import datetime
from account.models import Profile



def check_email_verify(user_id):
    return Profile.objects.filter(user_id=user_id).values()[0]['email_verify']
    
# Create your views here.
def month(request):
    # period = 31 days
    if request.user.is_authenticated:
        user_id = User.objects.filter(
            username=f'{request.user}').values()[0]['id']
        out_data = receive_and_pack(user_id=user_id, period='month')
    else:
        out_data = {}
    return render(request, 'user_stat/script.html', out_data)

def week(request):
    # period = 7 days
    if request.user.is_authenticated:
        user_id = User.objects.filter(
            username=f'{request.user}').values()[0]['id']
        out_data = receive_and_pack(user_id=user_id, period='week')
    else:
        out_data = {}
    return render(request, 'user_stat/script.html', out_data)

def day(request):
    # period = 1 days
    if request.user.is_authenticated:
        user_id = User.objects.filter(
            username=f'{request.user}').values()[0]['id']
        out_data = receive_and_pack(user_id=user_id, period='day')
    else:
        out_data = {}
    return render(request, 'user_stat/script.html', out_data)

def modification_for_week(records) -> list:
    now_week = datetime.now().isocalendar()[1]
    out_data = []
    for el in records:
        date = str(el.date)
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])
        week_number = int(datetime.date(
            datetime(year, month, day)).isocalendar()[1])
        if week_number == now_week and str(el.date)[0:4] == str(datetime.now())[0:4]:
            out_data.append(el)
    return out_data.copy()

def modification_for_day(records) -> list:
    now_day = str(datetime.now())[5:7]
    out_data = []
    for el in records:
        date = str(el.date)
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])
        day_number = int(str(datetime.date(
            datetime(year, month, day)))[5:7])
        if day_number == now_day and str(el.date)[0:4] == str(datetime.now())[0:4]:
            out_data.append(el)
    return out_data.copy()

def receive_and_pack(user_id, period) -> dict:
    all_debit_records = data.objects.filter(user_id=user_id).all()
    all_credit_records = credit.objects.filter(user_id=user_id).all()
    if period == 'month':
        debit_dict = make_out_data_month(all_debit_records)
        credit_dict = make_out_data_month(all_credit_records)
    elif period == 'week':
        debit_dict = make_out_data_week(all_debit_records)
        credit_dict = make_out_data_week(all_credit_records)
        all_debit_records = modification_for_week(all_debit_records)
        all_credit_records = modification_for_week(all_credit_records)
    elif period == 'day':
        debit_dict = make_out_data_day(all_debit_records)
        credit_dict = make_out_data_day(all_credit_records)
        all_debit_records = modification_for_day(all_debit_records)
        all_credit_records = modification_for_day(all_credit_records)
    debit_hist = make_histogram(all_debit_records)
    credit_hist = make_histogram(all_credit_records)
    median_credit = solve_median(credit_dict['amount'])
    median_debit = solve_median(debit_dict['amount'])
    is_verify = check_email_verify(user_id)
    out_data = {"debit_dict": debit_dict,
                "credit_dict": credit_dict,
                "median_credit": median_credit,
                "median_debit": median_debit,
                "hist_debit": debit_hist,
                "hist_credit": credit_hist,
                "verify": is_verify,
                }
    return out_data.copy()

def solve_median(list_of_amounts):
    median = 0
    for i in list_of_amounts:
        median += i
    median /= len(list_of_amounts)
    return round(median, 2)

def make_out_data_day(records):
    list_of_records_per_mounth = {'period': [],
                                  'amount': []
                                  }
    for i in range(32):
        list_of_records_per_mounth['amount'].append(0)
        list_of_records_per_mounth['period'].append(i)
    for el in records:
        for i in range(32):
            date = str(el.date)
            day = int(date[8:10])
            if day == i:
                list_of_records_per_mounth['amount'][i] += float(
                    round(el.amount))
    return list_of_records_per_mounth


def make_out_data_week(records):
    list_of_records_per_mounth = {'period': [],
                                  'amount': []
                                  }
    for i in range(53):
        list_of_records_per_mounth['amount'].append(0)
        list_of_records_per_mounth['period'].append(i)
    for el in records:
        for i in range(53):
            date = str(el.date)
            year = int(date[0:4])
            month = int(date[5:7])
            day = int(date[8:10])
            week_number = int(datetime.date(
                datetime(year, month, day)).isocalendar()[1])
            if week_number == i:
                list_of_records_per_mounth['amount'][i] += float(
                    round(el.amount))
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
                summ += float(el.amount)
        list_of_records_per_mounth['amount'].append(round(summ))
    return list_of_records_per_mounth.copy()


class histogram():
    _list_of_records_per_mounth = {'category': [],
                                   'amount': []}
    _records = None
    _summ = 0
    _summ_of_enother = 0

    def __init__(self, records) -> None:
        self._records = records
        self._list_of_records_per_mounth = {'category': [],
                                            'amount': []}
        for el in records:
            if not el.category in self._list_of_records_per_mounth['category']:
                self._list_of_records_per_mounth['category'].append(
                    el.category)
                self._list_of_records_per_mounth['amount'].append(0)

    def solve_amount(self):
        for el in self._records:
            self._summ += float(el.amount)

    def populating_lists(self):
        for i in range(len(self._list_of_records_per_mounth['category'])):
            category_amount = 0
            for el in self._records:
                if el.category == self._list_of_records_per_mounth['category'][i]:
                    category_amount += float(el.amount)
            if category_amount / self._summ > 0.01:
                self._list_of_records_per_mounth['amount'][i] = round(
                    category_amount)
            else:
                self._list_of_records_per_mounth['amount'][i] = 0
                self._summ_of_enother += float(el.amount)

    def removing_small_values(self):
        value = None
        size = 0
        while size != len(self._list_of_records_per_mounth['amount']):
            if self._list_of_records_per_mounth['amount'][size] == 0:
                value = size
                self._list_of_records_per_mounth['amount'].pop(size)
                size += 1
            size += 1
        if value != None:
            self._list_of_records_per_mounth['category'].pop(value)
            self._list_of_records_per_mounth['category'].append('другое')
            self._list_of_records_per_mounth['amount'].append(
                self._summ_of_enother)

    def get_histogram_data(self):
        return self._list_of_records_per_mounth.copy()

    def clear(self):
        self._list_of_records_per_mounth.clear()
        self._summ = 0
        self._records = None
        self._summ_of_enother = 0


def make_histogram(records):
    hist = histogram(records)
    hist.solve_amount()
    hist.populating_lists()
    hist.removing_small_values()
    out = hist.get_histogram_data()
    hist.clear()
    return out
