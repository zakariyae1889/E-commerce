from django.shortcuts import render
from django.views.generic import *

class EcommerceApp():
    #---------------------HomePage-----------------------#
    def PageHome(request):
        return render(request,template_name='Home/home.html')
    #---------------------ShopPage-----------------------#
    def PageShop(request):
        return render(request,template_name='Shop/shop.html')
    #---------------------ShopDetailsPage-----------------------#
    def PageShopDetail(request):
        return render(request,template_name='Shop/detail.html')
    #---------------------CartPage-----------------------#
    def PageCart(request):
        return render(request,template_name='Shop/cart.html')
    #---------------------CheckoutPage-----------------------#
    def PageCheckout(request):
        return render(request,template_name='Shop/checkout.html')
     
     
