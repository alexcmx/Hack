from django.forms import ModelForm, Form
from .models import Customers, Orders, Product
from django import forms


class RcvForm(Form):
    product = forms.CharField(label="Товар №", max_length=100)

class TakeForm(Form):
    order = forms.CharField(label="Заказ №",max_length=100)

