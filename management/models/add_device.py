from django.db import models
from datetime import date
from .add_model import Category_Brand

class Device(models.Model):
    resource_asset_number = models.CharField(max_length=255, null=False)
    purchase_date = models.DateField(default=date.today, null=False)
    model = models.ForeignKey(Category_Brand, on_delete=models.CASCADE, default=1, null=False)
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
    memory_size = models.CharField(max_length=10, default='64', null=False)
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
    supplier = models.CharField(max_length=255, null=False)
    production_date = models.DateField(default=date.today, null=False)
    bill_number = models.CharField(max_length=255, null=False)
    bill_image = models.ImageField(upload_to="uploads/bill_archive", null=False)

    def __int__(self):
        return self.resource_asset_number
