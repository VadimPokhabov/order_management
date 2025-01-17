from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from .forms import OrderForm


def add_order(request):
    if request.method == "POST":
        try:
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('view_orders')
        except TypeError:
            print("Ошибочка")
    else:
        form = OrderForm()
    return render(request, 'orders/add_order.html', {'form': form})


def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect('view_orders')


def view_orders(request):
    orders = Order.objects.all()
    return render(request, 'orders/view_orders.html', {'orders': orders})


def update_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('view_orders')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/update_order.html', {'form': form, 'order': order})


def add_product(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_orders')
    else:
        form = OrderForm()
    return render(request, 'product/add_product.html', {'form': form})


def delete_product(request, product_id):
    product = get_object_or_404(Order, id=product_id)
    product.delete()
    return redirect('view_orders')
