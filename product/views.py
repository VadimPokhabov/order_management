from django.shortcuts import render, redirect, get_object_or_404
from product.forms import ProductForm
from product.models import Product


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_orders')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('view_orders')
