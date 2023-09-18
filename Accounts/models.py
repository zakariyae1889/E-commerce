from django.db import models
from django.contrib.auth.models import User

class Profiles(models.Model):
    customer=models.OneToOneField(User,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='PhotoProfile')