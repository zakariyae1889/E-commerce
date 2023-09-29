from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from Product.models import *
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Product.form import FormReviews
from django.core.paginator import Paginator
# Create your views here.
class OrderApp():
    @login_required
    def Add_to_Cart(request,slug):
        product=get_object_or_404(Products,slug=slug)
        form=FormReviews()
          
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
               
       
               
        if 'quantity' in request.POST    and request.user.is_authenticated and not request.user.is_anonymous:
            
            qty=request.POST['quantity']
           
            
            order=Order.objects.filter(user=request.user, is_finished=False)
            if order:
                old_order=get_object_or_404(Order,user=request.user, is_finished=False)
                if OrderDetails.objects.filter(order=old_order,product=product).exists():
                   
                  orderitem=get_object_or_404(OrderDetails,order=old_order,product=product)
                  orderitem.quantity+=int(qty)
                  orderitem.save()
                else:
                   orderItem=OrderDetails.objects.create(product=product,order=old_order,quantity=qty)
                messages.success(request,"Was added to cart")
                return render(request,template_name='Shop/detail.html',  context=
                {
                    "product":product,
                    "form":form,
                    "reviews":Page_obj,
                    "rev_count":rev_count,
                })
               
            else:
               
                new_order=Order()
                new_order.user=request.user
                new_order.orderd_date=timezone.now()
                new_order.is_finished=False
                new_order.save()
                #-----------------------#
                orderItem=OrderDetails.objects.create(product=product,order=new_order,quantity=qty)
                orderItem.save()
                messages.success(request,"Was added to cart for new order")
                return render(request,template_name='Shop/detail.html',  context=
                {
                    "product":product,
                    "form":form,
                    "reviews":Page_obj,
                    "rev_count":rev_count,
                })
                
           
        return render(request,template_name='Shop/detail.html',  context=
        {
            "product":product,
            "form":form,
            "reviews":Page_obj,
            "rev_count":rev_count,
        })
    #----------------------------------------------#
     
   
    def PageCart(request):
        Orderdetails=None 
        order=None
        total=0
        if  request.user.is_authenticated and not request.user.is_anonymous:
            if Order.objects.filter(user=request.user,is_finished=False):
                order=get_object_or_404(Order,user=request.user,is_finished=False)
                Orderdetails=OrderDetails.objects.all().filter(order=order)
                total=0
                for sub in Orderdetails:
                    if sub.product.DiscountPrice:
                        total+=sub.quantity * sub.product.DiscountPrice
                    else : total+=sub.quantity * sub.product.Price
                
        return render(request,template_name="Shop/cart.html" ,  context={
            'order':order,
            'Orderdetails':Orderdetails,
            'total':total
           
        })
    #--------------------------------------------------------------------------#
    @login_required
    def Remove_from_Cart(request,id):
        if  request.user.is_authenticated and not request.user.is_anonymous and id:
            Orderdetails=get_object_or_404(OrderDetails,id=id)
            Orderdetails.delete()
            messages.error(request,"the  order is delete from your cart")
        return redirect('Path_Cart')
    #--------------------------------------------------------------------------#
    @login_required
    def add_qty(request,id):
        if  request.user.is_authenticated and not request.user.is_anonymous and id:
            orderdetails=get_object_or_404(OrderDetails,id=id)
            orderdetails.quantity+=1
            orderdetails.save()
            
        return redirect('Path_Cart')
    #--------------------------------------------------------------------------# 
    @login_required   
    def sub_qty(request,id):
        if  request.user.is_authenticated and not request.user.is_anonymous and id:
            orderdetails=get_object_or_404(OrderDetails,id=id)
            if orderdetails.quantity >1:
                orderdetails.quantity-=1
                orderdetails.save()
               
        return redirect('Path_Cart')
    #--------------------------------------------------------------------------# 
    @login_required
    def PageOrder(request):
        Orderdetails=None 
        order=None
        total=0
        if  request.user.is_authenticated and not request.user.is_anonymous:
                all_orders= Order.objects.filter(user=request.user)
                if all_orders:
                    for o in all_orders:
                        order=get_object_or_404(Order,id=o.id)
                        Orderdetails=OrderDetails.objects.all().filter(order=order)
                        total=0
                        for sub in Orderdetails:
                            if sub.product.DiscountPrice:
                                total+=sub.quantity * sub.product.DiscountPrice
                            else : total+=sub.quantity * sub.product.Price
                        o.total=total
                        o.items_count=Orderdetails.count
                
        return render(request,template_name="Shop/orders.html" ,  context={
           "all_orders":all_orders
           
        })




               

