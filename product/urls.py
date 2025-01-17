from django.urls import path
from .views import add_product, delete_product

urlpatterns = [
    path('add/', add_product, name='add_product'),
    path('delete/<int:product_id>/', delete_product, name='delete_product'),

]
