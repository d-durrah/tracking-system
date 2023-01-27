from django.db import models
from datetime import date
from .add_category import Category
from .add_brand import Brand
from .add_model import Model

class Device(models.Model):
    resource_asset_number = models.CharField(max_length=255, null=False)
    purchase_date = models.DateField(default=date.today, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, null=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1, null=False)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, default=1, null=False)
    memory = models.CharField(max_length=200, default='64GB', null=False)
    COLOR_CHOICES = [
        ('WHITE', 'White'),
        ('GRAY', 'Gray'),
        ('BLACK', 'Black'),
        ('RED', 'Red'),
        ('PINK', 'Pink'),
        ('BLUE', 'Blue'),
        ('GREEN', 'Green'),
        ('YELLOW', 'Yellow'),
        ('ORANGE', 'Orange'),
        ('PURPLE', 'Purple'),
    ]
    color = models.CharField(
        max_length=10,
        choices=COLOR_CHOICES,
        default='BLACK',
        null=False,
    )
    description = models.TextField(help_text="Add extra information", null=True)
    supplier = models.CharField(max_length=255, null=False)
    production_date = models.DateField(default=date.today, null=False)
    bill_number = models.CharField(max_length=255, null=False)
    bill_image = models.ImageField(upload_to="uploads/bill_archive", null=False)

    def __int__(self):
        return self.resource_asset_number
