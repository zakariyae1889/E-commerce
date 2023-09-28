from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('Home.urls')),
    path("",include('Product.urls')),
    path("",include('Order.urls')), 
    path("",include('Accounts.urls')),
    path("",include('Payment.urls')),
     
   
   
]
urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


