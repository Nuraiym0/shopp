from rest_framework.serializers import ModelSerializer
from .models import Comment, Reting


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class RetingSerializer(ModelSerializer):
    class Meta:
        model = Reting
        fields = '__all__'