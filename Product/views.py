from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator
from .models import *
from Order.models import *
from .form import FormReviews
from .filter import CategoryFliter
class ProductApp():
    #--------------------------------------------------------------------------------------------------------#
    def PageShop(request):
        
        product=Products.objects.all()

        MyfilterCategory=CategoryFliter(request.GET,queryset=product)
        product=MyfilterCategory.qs


       




        paginator=Paginator(product,6)
        page_number=request.GET.get('page')



      
        
      

        Page_obj=paginator.get_page(page_number)
        return render(
            request,
            template_name="Shop/shop.html",
            context={
                "product":Page_obj,
                "MyfilterCategory":MyfilterCategory,
                

                
        }
    )
    #--------------------------------------------------------------------------------------------------------#
    def PageShopDetails(request,slug):
        product=get_object_or_404(Products,slug=slug)
        
        
        reviews=Reviews.objects.filter(product=product)
        rev_count=reviews.count
        paginator=Paginator(reviews,3)
        page_number=request.GET.get('page')

        Page_obj=paginator.get_page(page_number)
        if request.method=='POST':
            form=FormReviews(request.POST)
            if form.is_valid():
                myform=form.save(commit=False)
              
                myform.product=product
                myform.save()
               
              

        else:form=FormReviews()
        return render(request,template_name='Shop/detail.html',  context=
        {
            "product":product,
            "form":form,
            "reviews":Page_obj,
            "rev_count":rev_count,
            
        })
    
    
    
     

