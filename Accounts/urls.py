from django.urls import path
from .views import *

urlpatterns = [
    path('SingUp/',AccountApp.PageRegister,name='SingUp')
]