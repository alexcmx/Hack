from .forms import RcvForm, TakeForm
from django.shortcuts import render
from .models import Product,Orders,Customers, Cells
# Create your views here.


def recv(request):
    if request.method == "GET": # Получаем пустую форму
        form = RcvForm()
        return render(request, 'Reception/recv.html', {'form': form})
    else: # Если отправляем форму
        form = RcvForm(request.POST)
        cell = ""
        if form.is_valid():

            data = form.cleaned_data
            this_prod = Product.objects.get(name=data['product']) # Объект товара
            this_prod.status="1" # Ставим статус что получили на складе
            this_prod.save()
            if this_prod.order.cell == None: # Если ячейка не назначена
                cell = Cells.objects.filter(empty=True)[0]
                this_prod.order.cell = cell
                cell.empty = False
                this_prod.order.save()
                this_prod.save()
                cell.save() # Назначили ячейку
                return render(request, 'Reception/recv2.html', {'Num': cell.pk})
            else:
                return render(request, 'Reception/recv2.html', {'Num': this_prod.order.cell.pk})

def take(request):
    if request.method == "GET":
        form = TakeForm()
        return render(request, 'Reception/take.html', {'form': form})
    else:
        form = TakeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ord = Orders.objects.get(Order_Id=data["order"])
            targ = Product.objects.filter(order=ord)
            targ1 = Product.objects.filter(order=ord).filter(status='1')
            targ2 = Product.objects.filter(order=ord).filter(status='0')
            f = True
            for i in targ:
                if i.status!='1':
                    f = False
            if f == True: # все на складе можно выдавать заказ
                done = "Заказ готов к выдаче"
            else:
                done = "Заказ еще не готов"
            fio = ord.customer.fio
            passport = ord.customer.passport
            cell = ord.cell.pk
            target1 = []
            target2 = []
            for i in targ1:
                target1.append(i.name)
            for i in targ2:
                target2.append(i.name)
            return render(request, 'Reception/take2.html', {'done':done,'fio':fio, 'pass': passport, 'cell': cell, 'target': target1, 'target2': target2})

def marks(request):
    if request.method == "GET":
        return render(request, "Reception/3.html")

def back(request):
    if request.method=="GET":
        return render(request, "Reception/2.html")


