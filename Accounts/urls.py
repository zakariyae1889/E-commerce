from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('Path_SingUp/',AccountApp.PageRegister,name='Path_SingUp'),
    path('Path_Profile/',AccountApp.PageProfile,name='Path_Profile'),
    path('Path_Edit_Profile/',AccountApp.PageEditProfile,name='Path_Edit_Profile'),
    path('Path_Login/',auth_views.LoginView.as_view(template_name="registering/login.html"),name='Path_Login'),
    path('Path_Logout/',auth_views.LogoutView.as_view(template_name="Home/home.html"),name='Path_Logout'),
]