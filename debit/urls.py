from django.urls import path
from . import views


urlpatterns = [
    path("credit/", views.view_credit.as_view()),
    path("debit/", views.view_debit.as_view()),
]
