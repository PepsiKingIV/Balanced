from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login/', views.user_login),
    path('registration/', views.register),
    path('', views.dashboard),
    path('logout/', views.logout_view, name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html', ),
         name='password_reset'),
]
