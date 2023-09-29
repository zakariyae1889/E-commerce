from django.shortcuts import render,get_object_or_404
from Order.models import *
from .form import PaymentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
class PaymentApp():
    @login_required
    def PagePayment(request): 
        if request.method=='POST':
            if  request.user.is_authenticated and not request.user.is_anonymous:
                if Order.objects.filter(user=request.user,is_finished=False):
                    order=get_object_or_404(Order,user=request.user,is_finished=False)
                    
                    Form=PaymentForm(request.POST)
                    if Form.is_valid():
                        myform=Form.save(commit=False)
                        myform.Order=order
                        myform.save()
                    order.is_finished=True
                    order.save()
                    messages.success(request,'Your order is finished')
                    
        else:
            Form=PaymentForm()
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
        return render(request,template_name="Shop/checkout.html" ,context={
            "Form":Form,
            'order':order,
            'Orderdetails':Orderdetails,
            'total':total
        })