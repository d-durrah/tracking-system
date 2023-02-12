from django.db import models
from .add_category import Category

class Supplier(models.Model):
    supplier = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, null=False)

    def __str__(self):
        return self.supplier