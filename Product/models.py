from django.db import models
from django.utils.text import slugify


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
    DiscountPrice=models.PositiveIntegerField(null=True,blank=True)
   
    photo=models.ImageField(upload_to='PhotoProduct/')
    
    slug=models.SlugField(blank=True,null=True)

    

    def save(self,*args,**kwargs):
        self.slug=slugify(self.Name)
        return super(Products,self).save(*args,**kwargs)
    
    def get_discount(self):
        Discount= self.DiscountPrice * (95/100)
        return Discount
    
    def __str__(self) -> str:
        return self.Name