from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import CategorySerializers, ProductSerializers
from .models import Category, Product
from .filters import ProductFilter



class CategoryViewSet(ModelViewSet):
    queryset  = Category.objects.all()
    serializer_class = CategorySerializers

class ProductViewSet(ModelViewSet):
    queryset  = Product.objects.all().order_by('id')
    serializer_class = ProductSerializers
    permission_classes = [IsAdminUser]
    # filterset_fields = ['category', 'status']
    filterset_class = ProductFilter


    def get_permissions(self):
        if self.action in ['retrieve', 'list','search']:
            # если это запрос на листинг или детализацию
            return [] # разрешаем всем
        return [IsAdminUser()] # разрешаем только админам


    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('q', openapi.IN_QUERY, type=openapi.TYPE_STRING)
        ])
    @action(['GET'], detail=False)
    def search(self, request):
        # /products/search/?q=hello
        # query_params = {'q':'hello'}
        q =request.query_params.get('q')
        qs = self.get_queryset() # get_queryset() - Product.object.all()
        if q:
            # qs = qs.filter(title__icontains=q)# title ilike '%hello%'
            qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q))  # title ilike '%hello%' or description ilike '%hello%'b
        pagination = self.paginate_queryset(qs)
        if pagination:
            serializer = self.get_serializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(qs, many=True) # get_serializer - ProductSerializer
        return Response(serializer.data, status=200)


