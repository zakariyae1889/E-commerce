from django.shortcuts import render,get_object_or_404
from .models import Profiles
from .form import RegisterForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

class AccountApp():
    def PageRegister(request):
        if request.method=="POST":
            formRegister=RegisterForm(request.POST,request.FILES)
            if formRegister.is_valid():
               formRegister.save()
               username=formRegister.cleaned_data["username"]
               password=formRegister.cleaned_data["password1"]
               photo=formRegister.cleaned_data["photo"]
               user=authenticate(username=username,password=password)
               pro=Profiles( customer=user,photo=photo)
               pro.save()
               login(request,user)
               return render(request, template_name="Home/home.html")
        else:formRegister=RegisterForm()
        return render(request,template_name='registering/SingUp.html' ,context={"formRegister":formRegister})
    #------------------------------------------#
    @login_required 
    def PageProfile(request):
        pro=get_object_or_404(Profiles,customer=request.user)
        return render(request, template_name="Profile/profiles.html",context={"pro":pro})
    