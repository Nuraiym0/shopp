from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializers, ProductSerializers
from .models import Category, Product



class CategoryViewSet(ModelViewSet):
    queryset  = Category.objects.all()
    serializer_class = CategorySerializers

class ProductViewSet(ModelViewSet):
    queryset  = Product.objects.all()
    serializer_class = ProductSerializers
