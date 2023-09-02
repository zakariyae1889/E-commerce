from django.urls import path

from . import views

urlpatterns = [
    #------------------Path_Home-----------------------------#
    path('',views.EcommerceApp.PageHome,name='Path_Home'),
    #------------------Path_Shop-----------------------------#
    path('Path_Shop/',views.EcommerceApp.PageShop,name='Path_Shop'),
    #------------------Path_Details_Shop-----------------------------#
    path('Path_Details_Shop/',views.EcommerceApp.PageShopDetail,name='Path_Details_Shop'),
    #------------------Path_Cart-----------------------------#
    path('Path_Cart/',views.EcommerceApp.PageCart,name='Path_Cart'),
    #------------------Path_Checkout-----------------------------#
    path('Path_Checkout/',views.EcommerceApp.PageCheckout,name='Path_Checkout'),
]