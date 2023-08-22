from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':"text", 'id': "exampleInputEmail1", 'aria-describedby':"emailHelp"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"type":"password", "class":"form-control", "id":"exampleInputPassword1"}))
