from django import forms
from .models import Payment
class PaymentForm(forms.ModelForm):
    class Meta:
        model=Payment
        fields=['ShipmentAddress','ShipmentPhone','cc_number','cc_expiry','cc_code']