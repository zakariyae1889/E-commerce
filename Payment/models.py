from django.db import models
from django.contrib.auth.models import User
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
# Create your models here.
class AddressShop(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Mobile=models.CharField(max_length=255)
    Address1=models.CharField(max_length=255)
    Address2=models.CharField(max_length=255)
    Country=models.CharField(max_length=255)
    City=models.CharField(max_length=255)
    State=models.CharField(max_length=255)
    ZipCode=models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.user.username

class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cc_number = CardNumberField(verbose_name='card number')
    cc_expiry = CardExpiryField(verbose_name='expiration date')
    cc_code = SecurityCodeField(verbose_name='security code')

    def __str__(self) -> str:
        return self.user.username
    