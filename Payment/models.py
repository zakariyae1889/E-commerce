from django.db import models
from django.contrib.auth.models import User
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from Order.models import Order


class Payment(models.Model):
    Order=models.ForeignKey(Order,on_delete=models.CASCADE)
    ShipmentAddress=models.CharField(max_length=255)
    ShipmentPhone=models.CharField(max_length=255)
    
    cc_number = CardNumberField(verbose_name='card number')
    cc_expiry = CardExpiryField(verbose_name='expiration')
    cc_code = SecurityCodeField(verbose_name='security code')

    def __str__(self) -> str:
        return self.Order.user.username

    
    