from django.db import models


class Order(models.Model):
    """Модель заказа"""

    STATUS_CHOICES = (
        ('pending', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),
    )

    table_number = models.IntegerField()
    items = models.JSONField()  # Список заказанных блюд с ценами
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def save(self, *args, **kwargs):
        # Автоматическое вычисление общей стоимости
        self.total_price = sum(item['price'] for item in self.items)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"Номер заказа {self.id} - номер стола {self.table_number} - состав заказа {self.items}"
