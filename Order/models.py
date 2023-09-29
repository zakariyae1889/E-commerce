from django.db import models
from Product.models import *
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
   
    start_date=models.DateTimeField(auto_now_add=True)
    orderd_date=models.DateTimeField()
    is_finished=models.BooleanField(default=False)
    total=0
    items_count=0

    def __str__(self) -> str:
        return self.user.username

class OrderDetails(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    
    quantity=models.PositiveIntegerField(default=1)
    
    def get_price(self):
        Price=self.quantity * self.product.Price
        return Price
    
    def get_discount(self):
        Discount=self.quantity * self.product.DiscountPrice 

        return Discount
    #--------------------#
    def get_total(self):
        if self.get_discount:
            self.total=self.get_discount()
        else:self.total=self.get_price()
    


       
                     
   
  


    def __str__(self) -> str:
        return self.product.Name