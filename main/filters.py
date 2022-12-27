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






# from django_filters.rest_framework import FilterSet
# import django_filters

# from .models import Course


# class CourseFilter(FilterSet):
#     users_filter = django_filters.CharFilter(field_name='author')
#     author_rating = django_filters.CharFilter(field_name='author__rating')
    
#     class Meta:
#         model = Course
#         fields = ['users_filter', 'author_rating']
