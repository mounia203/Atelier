from django import forms
from .models import OrderTable

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderTable
        fields = ['shipping_address']
