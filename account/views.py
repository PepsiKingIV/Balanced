from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user
from . import forms
from .models import Profile
import secrets, time
from threading import Thread


class EmailVerify(View):
    @staticmethod
    def get_user(uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            print(uid)
            user = User.objects.get(pk=uid)
        except (
            TypeError,
            ValueError,
            OverflowError,
            User.DoesNotExist,
            ValidationError,
        ):
            user = None
        return user

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)
        if user is not None and token_generator.check_token(user, token):
            print(user.id)
            Profile.objects.filter(user_id=user.id).update(email_verify=True)
            login(request, user)
            return redirect(to="http://127.0.0.1:8000/account/dashboard/")
        else:
            return redirect("http://127.0.0.1:8000/account/invalid_verify")


def user_menu(request):
    token = User.objects.filter(username=request.user).values()[0]["first_name"]
    return render(request, "account/dashboard.html", {"token": token})


def user_login(request):
    if request.user.is_authenticated:
        return redirect(to="http://127.0.0.1:8000/account/dashboard/")
    data = ""
    form = LoginForm(request.POST)
    if form.is_valid():
        user_data = form.cleaned_data
        user = authenticate(
            username=user_data["username"], password=user_data["password"]
        )
        if user is not None:
            user_data = User.objects.filter(username=request.POST["username"]).values()[0]
            user_id = user_data["id"]
            profile_data = Profile.objects.filter(user_id=user_id).values()[0]
            if user.is_active and profile_data["email_verify"]:
                login(request, user)
                profile_data.update(number_of_emails=0)
                if not Profile.objects.filter(user_id=user_id).exists():
                    Profile.objects.create(
                        user_id=user_id,
                        telegram_id="tel_id",
                        category={"debit": [], "credit": []},
                    )
                return redirect(to="http://127.0.0.1:8000/account/dashboard/")
            else:
                number_of_emails = profile_data["number_of_emails"]
                send_email_for_verify(request, user)
                number_of_emails += 1
                Profile.objects.filter(user_id=user_id).update(
                    number_of_emails=number_of_emails
                )
                if number_of_emails > 10:
                    User.objects.filter(id=user_id).update(is_active=False)
                data = "Вы не прошли верификацию по почте. На вашу почту было отправлено новое сообщение"
        else:
            data = "Неверный логин либо пароль"
        form = LoginForm()
    return render(request, "account/login.html", {"form": form, "data": data})


def send_email_for_verify(request, user, number_of_emails=0):
    current_site = get_current_site(request)
    context = {
        "domain": current_site.domain,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "user": user,
        "token": token_generator.make_token(user),
    }
    message = render_to_string("registration/verify_email.html", context=context)
    email = EmailMessage(
        "Верификация пользователя",
        message,
        to=[user.email],
    )
    email.send()


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        token = secrets.token_urlsafe()
        if user_form.is_valid():
            username = user_form.data["username"]
            email = user_form.cleaned_data["email"]
            password = user_form.data["password"]
            print(request.user)
            if User.objects.filter(username=username).exists():
                return render(
                    request,
                    "account/registr.html",
                    {
                        "user_form": user_form,
                        "data": "Пользователь с таким именем уже существует",
                    },
                )
            elif User.objects.filter(email=email).exists():
                return render(
                    request,
                    "account/registr.html",
                    {
                        "user_form": user_form,
                        "data": "Пользователь с такой почтой уже существует",
                    },
                )
            else:
                new_user = user_form.save(commit=False)
                new_user.first_name = token
                new_user.set_password(user_form.cleaned_data["password"])
                new_user.save()
                user_id = User.objects.filter(username=new_user.username).values()[0]["id"]
                Profile.objects.create(user_id=user_id)
                user = authenticate(username=username, password=password)
                send_email_for_verify(request, user=user)
                return redirect(to="http://127.0.0.1:8000/account/confirm_email/")
        else:
            return render(
                request,
                "account/registr.html",
                {
                    "user_form": user_form,
                    "data": "Пользователь с таким именем уже существует",
                },
            )
    else:
        user_form = UserRegistrationForm()
    return render(request, "account/registr.html", {"user_form": user_form})


def logout_view(request):
    logout(request)
    return redirect(to="http://127.0.0.1:8000/account/login/")


@login_required
def dashboard(request):
    return render(request, "account/dashboard.html", {"section": "dashboard"})


class PasswordResetView2(PasswordResetView):
    form_class = forms.PasswordResetForm2


class PasswordResetConfirmView2(PasswordResetConfirmView):
    form_class = forms.SetPasswordForm2


def new_token(request):
    token = secrets.token_urlsafe()
    old_token = User.objects.filter(username=f"{request.user}").values()[0]["first_name"]
    User.objects.filter(first_name=old_token).update(first_name=token)
    return redirect(to="http://127.0.0.1:8000/account/dashboard/")
