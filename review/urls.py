from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, RetingViewSet


router = DefaultRouter()
router.register('comments', CommentViewSet)
router.register('ratings', RetingViewSet)



urlpatterns = [
    path('', include(router.urls)),
]









