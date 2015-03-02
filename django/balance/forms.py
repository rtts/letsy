from django import forms

class TransactionForm(forms.Form):
    amount = forms.IntegerField(min_value=1)
    beneficiary = forms.EmailField
    description = forms.CharField(max_length=200)
