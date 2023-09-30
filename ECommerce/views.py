from django.shortcuts import render

def Errorhandel404(request,exception):
    return render(request,template_name="error/400.html",status=404)


def handel500(request,exception):
    return render(request,template_name="error/500.html")