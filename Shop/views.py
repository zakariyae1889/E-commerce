from django.shortcuts import render,get_object_or_404
from django.views.generic import *
from .models import *
#---------------------HomePage-----------------------#
class HomeViews():
   
    def PageHome(request):
        return render(request,template_name='Home/home.html')
#---------------------ShopPage-----------------------#
class ShopViews(ListView):
    model=Products
    template_name='Shop/shop.html'
    paginate_by=6
    context_object_name='product'
#---------------------ShopDetailsPage-----------------------#
class ShopDeatilsView(DetailView):
    model=Products
    template_name='Shop/detail.html'
    context_object_name='product'
#---------------------CartPage-----------------------#
class CartViews():
    def PageCart(request,slug):
        return render(request,template_name='Shop/cart.html')
#---------------------CheckoutPage-----------------------#
class CheckoutViews():
    def PageCheckout(request):
        return render(request,template_name='Shop/checkout.html')
     
