from django.forms import ModelForm, forms
from django import forms
from .models.loan_history import Log


class ResourceSignOutForm(ModelForm):
    class Meta:
        model = Log
        fields = ['resource_asset_number', 'item_description', 'purpose',
                  'ID_number', 'borrow_date', 'return_date']
