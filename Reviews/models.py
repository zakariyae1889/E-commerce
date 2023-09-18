from django.db import models
from  django.contrib.auth.models import User

class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Email=models.EmailField(unique=True,blank=True,null=True)
    Rating=models.PositiveSmallIntegerField()
    Review=models.TextField()
