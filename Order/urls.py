from django.urls import path

from .views import *

urlpatterns = [
    #------------------Path_Home-----------------------------#
    path('Path_Add_Cart/<str:slug>',OrderApp.Add_to_Cart,name='Path_Add_Cart'),
    path('Path_Cart/',OrderApp.PageCart,name='Path_Cart'),
    path('Path_Remove_Cart/<int:id>',OrderApp.Remove_from_Cart,name='Path_Remove_Cart'),
    path('Path_Add_Qty/<int:id>',OrderApp.add_qty,name='Path_Add_Qty'),
    path('Path_Sub_Qty/<int:id>',OrderApp.sub_qty,name='Path_Sub_Qty'),
]

