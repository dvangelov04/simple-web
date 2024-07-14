from .models import Stocks
from django import forms

class StockForm(forms.ModelForm):
    class Meta:
        model = Stocks
        fields = ['name', 'number', 'price']
        

        