from django.urls import include, path
from account.views import RegisterView, ChangePasswordView, UpdateProfileView, LogoutView, LogoutAllView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from rest_framework.routers import DefaultRouter

from .views import CustomTokenObtainPairView, TestAccount, UserProfileViewSet, api_list_view, delete_account, privacy

router = DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet, basename='userprofile')

urlpatterns = [
    path('list/', api_list_view, name='api_list'),
    path('login/', CustomTokenObtainPairView.as_view(), name='custom_login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
    path('test/', TestAccount.as_view(), name='test_account'),
    path('delete-account/', delete_account, name='delete_account'),
    path('privacy/', privacy, name='privacy'),
    path('', include(router.urls)),
]
