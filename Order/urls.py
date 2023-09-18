from django.urls import path

from .views import *

urlpatterns = [
    #------------------Path_Home-----------------------------#
    path('Path_Add_Cart/<str:slug>',OrderApp.Add_to_Cart,name='Path_Add_Cart'),
    path('Path_Cart/',OrderApp.PageCart,name='Path_Cart'),
]