from datetime import timedelta

from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinLengthValidator
from django.forms import ModelForm
from django.utils.datetime_safe import date
from management.models.add_asset import Asset
from .models.signatures import Signature
from .models.resource_signout_log import Log

# validation
numeric = RegexValidator(r'^\d+$', 'ID number must be 8 numeric values.')
length = MinLengthValidator(8, 'ID number must be 8 numeric values.')

class DateInput(forms.DateInput):
    input_type = 'date'


class ResourceSignOutForm(forms.Form):
    employee_ID = forms.ModelChoiceField(queryset=User.objects.all())
    resource_asset_number = forms.ModelChoiceField(queryset=Asset.objects.filter(available_to_borrow=True))
    purpose = forms.CharField(widget=forms.Textarea)
    sign_out_date = forms.DateField(initial=date.today, widget=DateInput())
    return_date = forms.DateField(initial=date.today, widget=DateInput())

    def clean(self):
        cleaned_data = super().clean()
        sign_out_date = cleaned_data.get("sign_out_date")
        return_date = cleaned_data.get("return_date")

        if sign_out_date and return_date and sign_out_date > return_date:
            self.add_error('return_date', "Return date should be after sign out date")

        if sign_out_date and return_date and (return_date - sign_out_date) > timedelta(days=30):
            self.add_error('return_date', "Return date should not be more than 1 month from sign out date")

        return cleaned_data


class SignatureForm(ModelForm):
    class Meta:
        model = Signature
        fields = ['signature', 'log_id']

    log_id = forms.ModelChoiceField(queryset=Log.objects.all(), widget=forms.HiddenInput())