from django.urls import path

from .views import *

urlpatterns = [
    #------------------Path_Home-----------------------------#
    path('',HomeApp.PageHome,name='Path_Home'),
]