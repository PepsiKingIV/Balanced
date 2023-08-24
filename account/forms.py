from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth import password_validation


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': "text", 'id': "exampleInputEmail1", 'aria-describedby': "emailHelp"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"type": "password", "class": "form-control", "id": "exampleInputPassword1"}))


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': "text", 'id': "exampleInputEmail1", 'aria-describedby': "emailHelp"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'type': "email", 'id': "exampleInputEmail1", 'aria-describedby': "emailHelp"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={"type": "password", "class": "form-control", "id": "exampleInputPassword1"}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(
        attrs={"type": "password", "class": "form-control", "id": "exampleInputPassword1"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class PasswordResetForm2(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'type': "email", 'id': "exampleInputEmail1", 'aria-describedby': "emailHelp"}))


class SetPasswordForm2(SetPasswordForm):
    new_password1 = forms.CharField(
        label=("Новый пароль"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "type": "password",
                                   "class": "form-control", "id": "exampleInputPassword1"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )

    new_password2 = forms.CharField(
        label=("Повторите пароль:"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "type": "password",
                                   "class": "form-control", "id": "exampleInputPassword1"}),
        strip=False
    )
