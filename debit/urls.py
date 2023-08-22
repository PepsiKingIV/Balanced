from django.urls import path
from . import views


urlpatterns = [
    path('credit/', views.credit),
    path('debit/', views.debit)
]