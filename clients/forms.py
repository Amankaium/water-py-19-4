from django import forms
from .models import Order, Client


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["name", "contacts", "description"]


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'address']
