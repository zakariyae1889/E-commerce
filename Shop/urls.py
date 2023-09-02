from django.urls import path

from .views import *

urlpatterns = [
    #------------------Path_Home-----------------------------#
    path('',HomeViews.PageHome,name='Path_Home'),
    #------------------Path_Shop-----------------------------#
    path('Path_Shop/',ShopViews.as_view(),name='Path_Shop'),
    #------------------Path_Details_Shop-----------------------------#
    path('Path_Details_Shop/<slug>', ShopDeatilsView.as_view(),name='Path_Details_Shop'),
    #------------------Path_Cart-----------------------------#
    path('Path_Cart/',CartViews.PageCart,name='Path_Cart'),
    #------------------Path_Checkout-----------------------------#
    path('Path_Checkout/',CheckoutViews.PageCheckout,name='Path_Checkout'),
]
