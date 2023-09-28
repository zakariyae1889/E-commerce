from django.urls import path
from . import views

urlpatterns = [
    path('path_payment',views.PaymentApp.PagePayment,name="path_payment")
]