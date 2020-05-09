from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Customers(models.Model):
    fio = models.CharField(max_length=255)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=17,
                                    blank=True)
    series = models.CharField(max_length=20)
    number = models.CharField(max_length=20)

class Orders(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.PROTECT)
    Order_Id = models.CharField(max_length=20, default="NONE")
    count = models.IntegerField(default=-1)
    money = models.IntegerField(default=-1)
    amount = models.IntegerField(default=-1)
    cell = models.OneToOneField(on_delete=models.SET_NULL, null=True, blank=True)

class Product(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, default="Default")

class Cells(models.Model):
    empty = models.BooleanField(default=True)
