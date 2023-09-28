from .models import Categorys,Products
def get_categorys(request):
    category=Categorys.objects.all()

    
    
    return {"category":category}

