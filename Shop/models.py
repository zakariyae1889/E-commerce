from django.db import models
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
# --------------------------------------------Create your models here-------------------------------------#.
type_color=(
    ('Red','Red'),
    ('Black','Black'),
    ('White','White'),
    ('Blue','Blue'),
    ('Green','Green')

    )
type_size=(
    ("XS","xs"),
    ("S","s"),
    ("M","m"),
    ("L","l"),
    ("XL","xl"),
    ("XXL","xxl"),

)
class Categorys(models.Model):
    Name=models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.Name
    
class Products(models.Model):
    category=models.ForeignKey(Categorys,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    Description=models.TextField(max_length=255)
    Price=models.PositiveIntegerField()
    DiscountPrice=models.PositiveIntegerField(null=True,blank=True)
   
    photo=models.ImageField(upload_to='PhotoProduct/')
    slug=models.SlugField(blank=True,null=True)

    

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        return super(Products,self).save(*args,**kwargs)
    
    def get_discount(self):
        Discount= self.DiscountPrice * (95/100)
        return Discount
    
    def __str__(self) -> str:
        return self.title

class OrderItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
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
        return self.product.title

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ItemOrder=models.ManyToManyField(OrderItem)
    start_date=models.DateTimeField(auto_now_add=True)
    orderd_date=models.DateTimeField()
    orderd=models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.user.username

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
    

class Reviews(models.Model):
    Name=models.CharField(max_length=255)
    Email=models.EmailField(unique=True,blank=True,null=True)
    Rating=models.PositiveSmallIntegerField()
    Review=models.TextField()
