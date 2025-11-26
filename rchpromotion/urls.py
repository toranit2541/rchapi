from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PromotionViewSet, TestRchpromotion

router = DefaultRouter()
router.register(r'promotion', PromotionViewSet, basename='promotion')

urlpatterns = [
    path('test/', TestRchpromotion.as_view(), name='test_promotion'),
    path('', include(router.urls)),
]