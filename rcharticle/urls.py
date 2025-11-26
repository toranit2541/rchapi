from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, TestRcharticle

router = DefaultRouter()
router.register(r'article', ArticleViewSet, basename='article')

urlpatterns = [
    path('test/',TestRcharticle.as_view(), name='test_account'),
    path('', include(router.urls)),
]