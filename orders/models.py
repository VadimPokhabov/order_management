from django.db import models

from product.models import Product


class Order(models.Model):
    """Модель заказа"""

    STATUS_CHOICES = (
        ('pending', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),
    )

    table_number = models.IntegerField()
    items = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"Номер заказа {self.id} - номер стола {self.table_number} - состав заказа {self.items}"


    @staticmethod
    def get_orders_by_id(ids):
        return Order.objects.filter(id__in=ids)

    @staticmethod
    def get_all_orders():
        return Order.objects.all()
