from django.db import models
from datetime import date
from management.models.add_asset import Asset


class Log(models.Model):
    asset_ID = models.ForeignKey(Asset, limit_choices_to={'available_to_borrow': True},
                                              on_delete=models.CASCADE)
    resource_asset_number = models.TextField(null=False)
    model = models.TextField(null=False)
    purpose = models.TextField(null=False)
    ID_number = models.CharField(max_length=8, null=False)
    borrow_date = models.DateField(default=date.today, null=False)
    return_date = models.DateField(default=date.today, null=False)
    returned = models.BooleanField(default=False)
    returned_on = models.DateField(null=True)

    class Meta:
        verbose_name = "Resource Sign-out Log"
        verbose_name_plural = "Resource Sign-out Logs"

    def __str__(self):
        return str(self.asset_ID)