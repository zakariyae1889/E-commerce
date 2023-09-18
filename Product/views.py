from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import *
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
    
     

