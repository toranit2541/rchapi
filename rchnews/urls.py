from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, TestRchnews

router = DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')

urlpatterns = [
    path('test/', TestRchnews.as_view(), name='test-rchnews'),
    path('', include(router.urls)),  # Adds versioning
]
