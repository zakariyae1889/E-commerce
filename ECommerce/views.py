from django.shortcuts import render

def custom_404(request, exception):
    return render(request, template_name='error/404.html', status=404)
