from django import forms
from django.core.validators import RegexValidator, MinLengthValidator
from django.forms import ModelForm
from django.utils.datetime_safe import date
from management.models.add_asset import Asset
from .models.signatures import Signature

# validation
numeric = RegexValidator(r'^\d+$', 'ID number must be 8 numeric values.')
length = MinLengthValidator(8, 'ID number must be 8 numeric values.')

class DateInput(forms.DateInput):
    input_type = 'date'


class ResourceSignOutForm(forms.Form):
    ID_number = forms.CharField(widget=forms.TextInput, validators=[numeric, length])
    asset_ID = forms.ModelChoiceField(queryset=Asset.objects.filter(available_to_borrow=True))
    purpose = forms.CharField(widget=forms.Textarea)
    borrow_date = forms.DateField(initial=date.today, widget=DateInput())
    return_date = forms.DateField(initial=date.today, widget=DateInput())

    def clean(self):
        cleaned_data = super().clean()
        borrow_date = cleaned_data.get("borrow_date")
        return_date = cleaned_data.get("return_date")

        if borrow_date and return_date and borrow_date > return_date:
            self.add_error('return_date', "Return date should be after borrow date")

        return cleaned_data


class SignatureForm(ModelForm):
    class Meta:
        model = Signature
        fields = ['signature']