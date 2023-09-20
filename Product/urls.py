from django.urls import path

from .views import *
urlpatterns = [
#------------------Path_Shop-----------------------------#
path('Path_Shop/',ProductApp.PageShop,name='Path_Shop'),
#------------------Path_Details_Shop-----------------------------#
path('Path_Details_Shop/<slug>',ProductApp.PageShopDetails,name='Path_Details_Shop'),


]
