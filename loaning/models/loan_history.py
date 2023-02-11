from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from datetime import date
from management.models.add_assets import Asset

# validation
numeric = RegexValidator(r'^\d+$', 'ID number must be 8 numeric values.')
length = MinLengthValidator(8, 'ID number must be 8 numeric values.')


class Log(models.Model):
    resource_asset_number = models.ForeignKey(Asset, limit_choices_to={'available_to_borrow': True},
                                              on_delete=models.CASCADE, null=False)
    item_description = models.TextField(null=False)
    purpose = models.TextField(null=False)
    ID_number = models.CharField(max_length=8, null=False, validators=[numeric, length])
    borrow_date = models.DateField(default=date.today, null=False)
    return_date = models.DateField(default=date.today, null=False)

    class Meta:
        verbose_name = "Loan History"
        verbose_name_plural = "Loan History"
