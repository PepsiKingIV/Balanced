from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views
from .views import EmailVerify
from django.views.generic import TemplateView

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
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
    path("password-reset/login/", views.user_login),
    path('registration/', views.register),
    path('confirm_email/', TemplateView.as_view(
        template_name='registration/confirm_email.html')),
    path('invalid_verify/', TemplateView.as_view(
        template_name='registration/invalid_verify.html')),
    path('', views.dashboard),
    path('logout/', views.logout_view, name='logout'),
    path('password-reset/',
         views.PasswordResetView2.as_view(), name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/',
         views.PasswordResetConfirmView2.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('generate-new-token/', views.new_token),
]
