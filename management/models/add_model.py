from django.db import models
from .add_category import Category
from .add_brand import Brand

class Category_Brand(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, null=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "model"
        verbose_name_plural = "models"