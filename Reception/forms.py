from django.forms import ModelForm, Form
from .models import Customers, Orders, Product
from django import forms

class RecieveForm(ModelForm):
    class Meta:
        model = Product
        fields = ''

class RcvForm(Form):
    order = forms.CharField(label="Заказ №:", max_length=100)
    product = forms.CharField(label="Товар №", max_length=100)