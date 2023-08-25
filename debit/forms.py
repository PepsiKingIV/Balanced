from django import forms
from .models import credit, debit


class debit_form(forms.Form):
    class Meta: 
        model = debit
        fields = ['user_id', 'date', 'amount', 'categoty']
    user_id = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': "text", 'id': "exampleInputEmail1", 'aria-describedby': "emailHelp"}))
    date = forms.DateField(widget=forms.DateInput(
        attrs={'id': "startDate", 'class': 'form-control', 'type': 'date'}))
    amount = forms.DecimalField(max_digits=9, decimal_places=2, widget=forms.NumberInput(
        attrs={'type': 'number', 'class': 'form-control', 'aria-label': 'amount'}))
    categoty = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': "text", 'id': "exampleInputEmail1", 'aria-describedby': "emailHelp"}))


class credit_form(forms.Form):
    user_id = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': "text", 'id': "exampleInputEmail1", 'aria-describedby': "emailHelp"}))
    date = forms.DateField(widget=forms.DateInput(
        attrs={'id': "startDate", 'class': 'form-control', 'type': 'date'}))
    amount = forms.DecimalField(max_digits=9, decimal_places=2, widget=forms.NumberInput(
        attrs={'type': 'number', 'class': 'form-control', 'aria-label': 'amount'}))
    categoty = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': "text", 'id': "exampleInputEmail1", 'aria-describedby': "emailHelp"}))
    priority = forms.IntegerField(max_value=10, widget=forms.NumberInput(
        attrs={'type': 'number', 'class': 'form-control', 'aria-label': 'amount'}))

class category(forms.Form):
    category = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': "text", 'id': "exampleInputEmail1", 'aria-describedby': "emailHelp"}))

    
    