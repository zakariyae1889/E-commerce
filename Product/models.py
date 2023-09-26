from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from Accounts.models import Profiles

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
    Name=models.CharField(max_length=255)
    Description=models.TextField()
    Price=models.PositiveIntegerField()
    DiscountPrice=models.PositiveIntegerField(null=True,blank=True,default=0)
   
    photo=models.ImageField(upload_to='PhotoProduct/')
    
    slug=models.SlugField(blank=True,null=True)

    

    def save(self,*args,**kwargs):
        self.slug=slugify(self.Name)
        return super(Products,self).save(*args,**kwargs)
    
    def get_discount(self):
        Discount= self.DiscountPrice 
        return Discount
    

    def __str__(self) -> str:
        return self.Name
    
class Reviews(models.Model):

    Name=models.CharField(max_length=255)
    Email=models.EmailField(max_length=255)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    Review=models.TextField()
    data=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.Name