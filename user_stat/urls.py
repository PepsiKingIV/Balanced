from django.urls import path
from . import views


urlpatterns = [
    path("", views.month),
    path("month/", views.month),
    path("week/", views.week),
    path("day/", views.day),
]
