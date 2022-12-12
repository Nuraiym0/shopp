from rest_framework.viewsets import ModelViewSet
from .serializers import CommentSerializer, RetingSerializer
from .models import Comment, Reting

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class RetingViewSet(ModelViewSet):
    queryset = Reting.objects.all()
    serializer_class = RetingSerializer






