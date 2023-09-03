from django.forms import ModelForm
from .models import *
class CartForm(ModelForm):
    class Meta:
        model=OrderItem
        fields=["size","color","quantity"]