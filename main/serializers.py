from rest_framework.serializers import ModelSerializer
from .models import Category, Product

class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializers(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'