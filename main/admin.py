from django.contrib import admin
from .models import Category, Product
from review.models import Comment, Reting

class RetingInLine(admin.TabularInline):
    model = Reting


class CommentInLine(admin.TabularInline):
    model = Comment
    

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status']
    list_filter = ['category', 'status']
    search_fields = ['title','description']
    inlines = [CommentInLine, RetingInLine]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
