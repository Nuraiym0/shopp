from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import CommentSerializer, RetingSerializer
from .models import Comment, Reting
from .permissions import IsAuthorOrReadOnly

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]


# class RetingViewSet(ModelViewSet):
#     queryset = Reting.objects.all()
#     serializer_class = RetingSerializer
#     permission_classes = [IsAuthorOrReadOnly]


class CreateRatingAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=RetingSerializer())
    def post(self, request):
        user = request.user
        ser = RetingSerializer(data=request.data, context = {'request':request})
        ser.is_valid(raise_exception=True)
        product_id = request.data.get('product')
        if Reting.objects.filter(author=user, product__id=product_id).exists():
            rating = Reting.objects.get(author=user, product__id=product_id)
            rating.value = request.data.get('value')
            rating.save()
        else:
            # Reting.objects.create(user)
            ser.save()
        return Response (status=201)

        



