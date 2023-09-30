from django.shortcuts import render,get_object_or_404,redirect
from .models import Profiles
from .form import RegisterForm,ProfileForm,UserForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
    #------------------------------------------#
    @login_required
    def PageEditProfile(request):
        profile=get_object_or_404(Profiles, customer=request.user)
        if request.method=="POST":
            formuser=UserForm(request.POST,instance=request.user)
            formprofile=ProfileForm(request.POST,request.FILES,instance=profile)
            if formuser.is_valid() and formprofile.is_valid():
                formuser.save()
                myprofile=formprofile.save(commit=False)
                myprofile.user=request.user
                myprofile.save()
                messages.success(request,"Profiles Edit Successfully")
                return redirect("Path_Profile")
        else:
            formuser=UserForm(instance=request.user)
            formprofile=ProfileForm(instance=profile)
        return render(request,template_name="Profile/EditProfile.html", context={
            "formuser":formuser,
            "formprofile":formprofile,
        })

    