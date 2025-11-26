from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import PtLabResViewSet, PatientInHosViewSet, LabApplicationViewSet, PatientDataViewSet, LabResultDetailViewSet, VResultAppViewSet, get_lab_results, get_lab_results_dynamic, get_vresult, get_VnDate, get_labresults_by_app

router = DefaultRouter()
router.register(r'pt_lab_res', PtLabResViewSet)
router.register(r'patient_in_hos', PatientInHosViewSet)
router.register(r'patient_data', PatientDataViewSet)
router.register(r'lab_application', LabApplicationViewSet)
router.register(r'lab_result_detail', LabResultDetailViewSet)
router.register(r'v_result_app', VResultAppViewSet)
# router.register(r'VResult',get_vresult, basename='VResult')
# router.register(r'lab-results',get_lab_results, basename='lab-results')
# router.register(r'lab-results-dynamic',get_lab_results_dynamic, basename='lab-results-dynamic')

urlpatterns = [
    path('test/', views.TestRchdata.as_view(), name='test_rchdata'),
    path('VResult/', get_vresult, name='get_vresult'),
    path("lab-results/", get_lab_results, name="lab_results"),
    path("lab-results-bydate/", get_lab_results, name="lab_results-bydate"),
    path('lab-results-dynamic/', get_lab_results_dynamic, name='lab-results-dynamic'),
    path('lab-results-byapp/',get_labresults_by_app,name ="labresults-byapp"),
    path('lab-vndate/',get_VnDate,name='lab-vndate'),
    path('', include(router.urls)),
]