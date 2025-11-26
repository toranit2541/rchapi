from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventQueryView, EventViewSet, TestRchEven

router = DefaultRouter()
router.register(r'even', EventViewSet)

urlpatterns = [
    path('test/', TestRchEven.as_view(), name='test_event'),
    path('evens/', EventQueryView.as_view(), name='even_query'),
    path('', include(router.urls)),
]