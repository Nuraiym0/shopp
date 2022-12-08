from django_filters.rest_framework import FilterSet
import django_filters

from .models import Product


class ProductFilter(FilterSet):
    categoty_id = django_filters.NumberFilter(field_name='category')
    category_title = django_filters.CharFilter(field_name='category__title')
    # status = 
    class Meta:
        model = Product
        fields = ['category_id', 'category_title', 'status']




