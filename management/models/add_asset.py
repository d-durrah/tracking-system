from django.db import models
from datetime import date
from smart_selects.db_fields import ChainedForeignKey
from .add_device import Device
from .add_category import Category
from .add_supplier import Supplier


class Asset(models.Model):
    resource_asset_number = models.CharField(max_length=255, null=False)
    purchase_date = models.DateField(default=date.today, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, null=False)
    supplier = ChainedForeignKey(
        Supplier,
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True,
        sort=True)
    model = ChainedForeignKey(
        Device,
        chained_field="supplier",
        chained_model_field="supplier",
        show_all=False,
        auto_choose=True,
        sort=True)
    MEMORY_SIZE_CHOICES = [
        ('2', '2GB'),
        ('4', '4GB'),
        ('8', '8GB'),
        ('12', '12GB'),
        ('16', '16GB'),
        ('18', '18GB'),
        ('24', '24GB'),
        ('32', '32GB'),
        ('64', '64GB'),
        ('48', '48GB'),
        ('128', '128GB'),
        ('256', '256GB'),
    ]
    memory_size = models.CharField(max_length=10, choices=MEMORY_SIZE_CHOICES, default='64', null=False)
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
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default='BLACK', null=False)
    description = models.TextField(help_text="Add extra information", null=True)
    production_date = models.DateField(default=date.today, null=False)
    bill_number = models.CharField(max_length=255, null=False)
    bill_image = models.ImageField(upload_to="uploads/bill_archive", null=False)
    available_to_borrow = models.BooleanField(default=True)

    def __str__(self):
        return self.resource_asset_number

    class Meta:
        verbose_name = "CCIT Asset"
        verbose_name_plural = "CCIT Asset"