from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PackageViewSet, TestRchpackage

router = DefaultRouter()
router.register(r'package', PackageViewSet, basename='package')

urlpatterns = [
    path('test/', TestRchpackage.as_view(), name='test_package'),
    path('', include(router.urls)),
]