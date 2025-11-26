from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PopulationViewSet, TestRchpopulation

router = DefaultRouter()
router.register(r'population', PopulationViewSet, basename='population')

urlpatterns = [
    path('test/', TestRchpopulation.as_view(), name='test_population'),
    path('', include(router.urls)),
]