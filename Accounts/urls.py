from django.urls import path,reverse_lazy
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    #------------------PathSingUp-----------------#
    path(
        'Path_SingUp/',
         AccountApp.PageRegister,
         name='Path_SingUp'
         ),
    #------------------PathProfile-----------------#
    path(
        'Path_Profile/',
         AccountApp.PageProfile,
         name='Path_Profile'
    ),
    #------------------PathEditProfile-----------------#
    path(
        'Path_Edit_Profile/',
        AccountApp.PageEditProfile,
        name='Path_Edit_Profile'
    ),
    #------------------PathLogin-----------------#
    path(

        'Path_Login/',
        auth_views.LoginView.as_view(template_name="registering/login.html"),
        name='Path_Login'
    ),
    #------------------PathLogout-----------------#
    path(
        'Path_Logout/',
        auth_views.LogoutView.as_view(template_name="Home/home.html"),
        name='Path_Logout'
    ),
    #------------------PathChangePassword-----------------#
    path(
        "Path_Change_Passowrd",
        auth_views.PasswordChangeView.as_view(
        template_name="password/password_change_form.html",
        success_url=reverse_lazy('Path_Change_Passowrd_Done')
        ), 
        name="Path_Change_Passowrd"
    ),
    #------------------PathChangePasswordDoneView-----------------#
    path(
        "Path_Change_Passowrd_Done",
        auth_views.PasswordChangeDoneView.as_view( 
            template_name="password/password_change_done.html"
        ), 
        name="Path_Change_Passowrd_Done"),
]