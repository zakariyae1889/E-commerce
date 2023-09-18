from django.shortcuts import render

# Create your views here.
class AccountApp():
    def PageRegister(request):
        return render(request,template_name='registering/SingUp.html')