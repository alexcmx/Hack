from .forms import RcvForm
from django.shortcuts import render
from .models import Product,Orders,Customers
# Create your views here.


def recv(request):
    if request.method == "GET":
        form = RcvForm()
        return render(request, 'Reception/recv.html', {'form': form})
    else:
        form = RcvForm(request.POST)
        this_order = Orders.objects.get(Order_Id=form.order)
        this_prod = Product.objects.get(name=form.product)
        if this_order.cell < 1:

