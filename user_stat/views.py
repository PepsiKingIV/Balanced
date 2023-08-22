from django.shortcuts import render

# Create your views here.
def stat(request):
    return render(request, 'user_stat/stat.html')