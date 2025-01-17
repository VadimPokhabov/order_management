from django.urls import path
from .views import add_order, delete_order, view_orders, update_order

urlpatterns = [
    path('add/', add_order, name='add_order'),
    path('delete/<int:order_id>/', delete_order, name='delete_order'),
    path('', view_orders, name='view_orders'),
    path('update/<int:order_id>/', update_order, name='update_order'),
]
