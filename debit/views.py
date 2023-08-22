from django.shortcuts import render


def debit(request):
    return render(request, 'debit/debit.html')

def credit(request):
    return render(request, 'debit/credit.html')
