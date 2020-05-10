from .forms import RcvForm
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



