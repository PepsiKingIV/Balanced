from django.shortcuts import render


def index(request):
    
    return render(request, "main/index.html")

def consent(request):
    return render(request, 'main/consent.html')