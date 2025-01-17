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

    # @staticmethod
    # def get_products_by_id(ids):
    #     return Product.objects.filter(id__in=ids)
    #
    # @staticmethod
    # def get_all_products():
    #     return Product.objects.all()
