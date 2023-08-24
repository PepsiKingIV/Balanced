from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

from django.urls import path

from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('login/', views.user_login),
    path("password-reset/login/", views.user_login),
    path('registration/', views.register),
    path('', views.dashboard),
    path('logout/', views.logout_view, name='logout'),
    path('password-reset/', 
            views.PasswordResetView2.as_view(),name='password_reset'),
    path('password-reset/done/',
            PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/',
            views.PasswordResetConfirmView2.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/',
            PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
