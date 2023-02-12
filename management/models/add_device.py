from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from .add_category import Category
from .add_supplier import Supplier

class Device(models.Model):
    name = models.CharField(max_length=100, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, null=False)
    supplier = ChainedForeignKey(
        Supplier,
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True,
        sort=True)

    def __str__(self):
        return self.name