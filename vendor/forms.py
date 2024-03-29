from django import forms
from .models import Vendor
from accounts.validators import allow_images


class VendorForm(forms.ModelForm):
    vendor_license = forms.FileField(widget=forms.FileInput(attrs={'class':'btn btn-info'}),validators=[allow_images])
    class Meta:
        model = Vendor
        fields = ['vendor_name','vendor_license']