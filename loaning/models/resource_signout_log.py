from django.db import models
from datetime import date
from management.models.add_asset import Asset


class Log(models.Model):
    asset_ID = models.IntegerField(null=False)
    resource_asset_number = models.CharField(max_length=255, null=False)
    model = models.CharField(max_length=255, null=False)
    purpose = models.TextField(null=False)
    employee_ID = models.CharField(max_length=8, null=False)
    name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    sign_out_date = models.DateField(default=date.today, null=False)
    return_date = models.DateField(default=date.today, null=False)
    returned = models.BooleanField(default=False)
    returned_on = models.DateField(null=True)

    class Meta:
        verbose_name = "Resource Sign-out Log"
        verbose_name_plural = "Resource Sign-out Logs"

    def __str__(self):
        return str(self.id)