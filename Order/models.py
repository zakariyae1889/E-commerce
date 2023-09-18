from django.db import models
from Product.models import *
from django.contrib.auth.models import User
# Create your models here.
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
   
    start_date=models.DateTimeField(auto_now_add=True)
    orderd_date=models.DateTimeField()
    is_finished=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username

class OrderDetails(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    color=models.CharField(max_length=255,choices=type_color,default='White')
    size=models.CharField(max_length=255,choices=type_size,default='S')
    quantity=models.PositiveIntegerField()
    
    def get_price(self):
        Price=self.quantity * self.product.Price
        return Price
    
    def get_discount(self):
        Discount=self.quantity * (self.product.DiscountPrice * (5/100))
        return Discount
    
    def get_Total(self):
        if self.get_discount() > 0:
            total=self.get_discount()
        else: 
            total=self.get_price()
        return total
    
  


    def __str__(self) -> str:
        return self.product.Name