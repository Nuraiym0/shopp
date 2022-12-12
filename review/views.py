from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import CommentSerializer, RetingSerializer
from .models import Comment, Reting
from .permissions import IsAuthorOrReadOnly

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]


class RetingViewSet(ModelViewSet):
    queryset = Reting.objects.all()
    serializer_class = RetingSerializer
    permission_classes = [IsAuthorOrReadOnly]






