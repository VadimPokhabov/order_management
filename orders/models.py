from django.db import models


class Product(models.Model):
    """Модель продукта"""
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.CharField(max_length=250, blank=True, null=True)

    class Mets:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f"Наименование продукта {self.name}, цена продукта {self.price}, описание {self.description}"

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()


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
