import django_filters
from .models import Products
from Order.models import OrderDetails

class CategoryFliter(django_filters.FilterSet):
    class Meta:
        
        model=Products
        fields=["category"]

class ColorFilter(django_filters.FilterSet):
    class Meta:


        model=OrderDetails
        fields=["color"]

class SizeFilter(django_filters.FilterSet):
    class Meta:


        model=OrderDetails
        fields=["size"]