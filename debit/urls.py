from django.urls import path
from . import views


urlpatterns = [
    path("credit/", views.v_credit),
    path("debit/", views.view_debit.as_view()),
]
