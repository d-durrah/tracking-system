from django.core.validators import RegexValidator, MinLengthValidator
from django import forms
from django.utils.datetime_safe import date
from management.models.add_asset import Asset

# validation
numeric = RegexValidator(r'^\d+$', 'ID number must be 8 numeric values.')
length = MinLengthValidator(8, 'ID number must be 8 numeric values.')

class DateInput(forms.DateInput):
    input_type = 'date'


class ResourceSignOutForm(forms.Form):
    ID_number = forms.CharField(widget=forms.TextInput, validators=[numeric, length])
    resource_asset_number = forms.ModelChoiceField(queryset=Asset.objects.filter(available_to_borrow=True))
    purpose = forms.CharField(widget=forms.Textarea)
    borrow_date = forms.DateField(initial=date.today, widget=DateInput())
    return_date = forms.DateField(initial=date.today, widget=DateInput())