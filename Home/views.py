from django.shortcuts import render

class HomeApp():
    def PageHome(request):
        return render(request,template_name="Home/home.html")
