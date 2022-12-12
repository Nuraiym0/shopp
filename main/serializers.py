from rest_framework.serializers import ModelSerializer
from .models import Category, Product
from review.serializers import CommentSerializer

class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializers(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



    def to_representation(self, instance: Product):
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializers(instance.category).data
        rep['comments'] = CommentSerializer(instance.comments.all(), many = True).data 
        return rep