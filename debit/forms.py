from django import forms
from account.models import userСategories


class debit_form(forms.Form):

    date = forms.DateField(widget=forms.DateInput(
        attrs={'id': "startDate", 'class': 'form-control', 'type': 'date'}))
    amount = forms.DecimalField(max_digits=9, decimal_places=2, widget=forms.NumberInput(
        attrs={'type': 'number', 'class': 'form-control', 'aria-label': 'amount'}))
    category = forms.ChoiceField(choices=[], required=True, widget=forms.Select(
        attrs={'class': 'form-control form-control-lg  select', 'style': 'font-size: 1rem;'}))
    
    def create_db_form(self, user_id, request):
        out_form = {
                'user_id' : user_id,
                'date' : request.POST['date'],
                'category' : request.POST['category'],
                'amount' : request.POST['amount'],
        }
        return out_form

    def add_choices(self, list_of_choices):
        choices = []
        for i in list_of_choices:
            choices.append([i, i])
        self.base_fields['category'].choices = choices

class credit_form(forms.Form):

    date = forms.DateField(widget=forms.DateInput(
        attrs={'id': "startDate", 'class': 'form-control', 'type': 'date'}))
    amount = forms.DecimalField(max_digits=9, decimal_places=2, widget=forms.NumberInput(
        attrs={'type': 'number', 'class': 'form-control', 'aria-label': 'amount'}))
    category = forms.ChoiceField(choices=[], required=True, widget=forms.Select(
        attrs={'class': 'form-control form-control-lg  select', 'style': 'font-size: 1rem;'}))
    priority = forms.IntegerField(max_value=10, widget=forms.NumberInput(
        attrs={'type': 'number', 'class': 'form-control', 'aria-label': 'amount'}))

    def create_db_form(self, user_id, request):
        out_form = {
                'user_id' : user_id,
                'date' : request.POST['date'],
                'category' : request.POST['category'],
                'amount' : request.POST['amount'],
                'priority' : request.POST['priority']
        }
        return out_form
    
    def add_choices(self, list_of_choices):
        choices = []
        for i in list_of_choices:
            choices.append([i, i])
        self.base_fields['category'].choices = choices
        
    

class category(forms.Form):
    category = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': "text", 'id': "exampleInputEmail1", 'aria-describedby': "emailHelp"}))


class delete_record(forms.Form):
    record_id = forms.IntegerField(max_value=10, widget=forms.NumberInput(
        attrs={'type': 'number', 'class': 'form-control', 'aria-label': 'amount'}))
