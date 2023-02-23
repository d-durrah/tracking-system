from django.db import models
from datetime import date
from management.models.add_asset import Asset

class Logg(models.Model):
    ID_number = models.CharField(max_length=8, null=False)
    resource_asset_number = models.ForeignKey(Asset, limit_choices_to={'available_to_borrow': True},
                                              on_delete=models.CASCADE, null=False)
    item_description = models.TextField(null=False)
    purpose = models.TextField(null=False)
    borrow_date = models.DateField(default=date.today, null=False)
    return_date = models.DateField(default=date.today, null=False)

    class Meta:
        verbose_name = "Loan History"
        verbose_name_plural = "Loan History"
