from django import forms
from account.models import userСategories


class debit_form(forms.Form):
    
    date = forms.DateField(widget=forms.DateInput(
        attrs={'id': "startDate", 'class': 'form-control', 'type': 'date'}))
    amount = forms.DecimalField(max_digits=9, decimal_places=2, widget=forms.NumberInput(
        attrs={'type': 'number', 'class': 'form-control', 'aria-label': 'amount'}))
    category = forms.ChoiceField(choices=[] ,required=True, widget=forms.Select(attrs={'class':'form-control form-control-lg  select', 'style':'font-size: 1rem;'}))


class credit_form(forms.Form):
    
    date = forms.DateField(widget=forms.DateInput(
        attrs={'id': "startDate", 'class': 'form-control', 'type': 'date'}))
    amount = forms.DecimalField(max_digits=9, decimal_places=2, widget=forms.NumberInput(
        attrs={'type': 'number', 'class': 'form-control', 'aria-label': 'amount'}))
    category = forms.ChoiceField(choices=[] ,required=True, widget=forms.Select(attrs={'class':'form-control form-control-lg  select', 'style':'font-size: 1rem;'}))
    priority = forms.IntegerField(max_value=10, widget=forms.NumberInput(
        attrs={'type': 'number', 'class': 'form-control', 'aria-label': 'amount'}))

class category(forms.Form):
    category = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': "text", 'id': "exampleInputEmail1", 'aria-describedby': "emailHelp"}))

class delete_record(forms.Form):
    record_id = forms.CharField(max_length=10)