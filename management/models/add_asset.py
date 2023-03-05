from django.db import models
from datetime import date, datetime


class Asset(models.Model):
    asset_id = models.CharField(max_length=100, null=False)
    resource_asset_number = models.CharField(max_length=255, null=True)
    model = models.CharField(max_length=255, null=False)
    manufacturer = models.CharField(max_length=255, null=False)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    user_email = models.CharField(max_length=255, null=False)
    purchase_date = models.DateTimeField(default=datetime.today, null=True)
    bill_number = models.CharField(max_length=255, null=True)
    bill_image = models.ImageField(upload_to="uploads/bill_archive", null=True)
    available_to_borrow = models.BooleanField(default=True)

    def __str__(self):
        return str(self.asset_id)

    class Meta:
        verbose_name = "CCIT Asset"
        verbose_name_plural = "CCIT Assets"