from django import forms
from .models import Order, Product


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['table_number', 'items']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']
