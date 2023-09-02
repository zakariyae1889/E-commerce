from django.conf import settings
from django.views.static import serve
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('Shop.urls')),
    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$',serve,{'document_root':settings.STATIC_ROOT}),
]
#urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
#urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
handler404="ECommerce.views.custom_404"

