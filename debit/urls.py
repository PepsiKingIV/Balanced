from django.urls import path, include, re_path
from .views import *


urlpatterns = [
    path("credit/", view_credit.as_view()),
    path("debit/", view_debit.as_view()),
    path("api/debit/", DebitAPIList.as_view()),
    path("api/credit/", CreditAPIList.as_view()),
    path("api/auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.authtoken")),
]
