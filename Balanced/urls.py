from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('main.urls')),
    path("data/", include('debit.urls')),
    path("statistics/", include('user_stat.urls')),
    path("account/", include('account.urls')),
]
