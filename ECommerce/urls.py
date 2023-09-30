from django.conf import settings
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.views.static import serve 

handeler404='ECommerce.views.Errorhandel404'
handeler500='ECommerce.views.handel500'
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('Home.urls')),
    path("",include('Product.urls')),
    path("",include('Order.urls')), 
    path("",include('Accounts.urls')),
    path("",include('Payment.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
   
   
]

urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.logout_template='Home/home.html'




