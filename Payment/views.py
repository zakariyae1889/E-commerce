from django.shortcuts import render

# Create your views here.
class PaymentApp():
    def PagePayment(request):
        return render(request,template_name="Shop/checkout.html")