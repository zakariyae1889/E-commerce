from .models import Categorys,Products
def get_categorys(request):
    category=Categorys.objects.all()

    
    
    return {"category":category}

def filter_category():
    category=Categorys.objects.all()

    filterCategory=Products.objects.filter(category=category)

    return {"filterCategory":filterCategory}

