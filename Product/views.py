from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator
from .models import *
from Order.models import *
class ProductApp():
    #--------------------------------------------------------------------------------------------------------#
    def PageShop(request):
        product=Products.objects.all()
        paginator=Paginator(product,6)
        page_number=request.GET.get('page')

        Page_obj=paginator.get_page(page_number)
        return render(
            request,
            template_name="Shop/shop.html",
            context={
                "product":Page_obj
        }
    )
    #--------------------------------------------------------------------------------------------------------#
    def PageShopDetails(request,slug):
        product=get_object_or_404(Products,slug=slug)
        return render(request,template_name='Shop/detail.html', context={"product":product})
    
    def add_qty(request,id):
        if  request.user.is_authenticated and not request.user.is_anonymous and id:
            orderdetails=get_object_or_404(OrderDetails,id=id)
            orderdetails.quantity+=1
            orderdetails.save()
            
        return render(request,template_name='Shop/detail.html', context={"orderdetails":orderdetails})
        
       


      
    
    def sub_qty(request,id):
        if  request.user.is_authenticated and not request.user.is_anonymous and id:
            orderdetails=get_object_or_404(OrderDetails,id=id)
            if orderdetails.quantity >1:
                orderdetails.quantity-=1
                orderdetails.save()
               
        return render(request,template_name='Shop/detail.html', context={"orderdetails":orderdetails})
        
    
     

