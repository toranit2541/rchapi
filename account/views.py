from django.shortcuts import render
from account.models import Account, UserProfile
from .serializers import RegisterSerializer, ChangePasswordSerializer, UpdateUserSerializer, UserProfileSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework import viewsets
from rest_framework.throttling import UserRateThrottle
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import get_resolver
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            # ✅ Add message to successful login
            response.data['message'] = "Login successful!"
            return response
        else:
            # ❌ response.data may not exist or be writable here
            return Response(
                {"error": "Invalid username or password"},
                status=response.status_code
            )

class RegisterView(generics.CreateAPIView):
    qqueryset = Account.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    throttle_classes = [UserRateThrottle]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # Include additional data in the response, such as a login URL or token
        response.data['message'] = "Registration successful! Please log in."
        response.data['login_url'] = "/auth/login/"
        return response


class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateProfileView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Invalid token or request."}, status=status.HTTP_400_BAD_REQUEST)


class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user profiles to be viewed or edited.
    """
    queryset = User.objects.all()  # Use the built-in User model
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:  # Admin users see all
            return User.objects.all()
        return User.objects.filter(username=self.request.user.username)
        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_list_view(request):
    # List all available APIs dynamically
    url_resolver = get_resolver()
    api_urls = []
    for pattern in url_resolver.url_patterns:
        if hasattr(pattern, 'pattern'):
            api_urls.append(str(pattern.pattern))

    return JsonResponse({'api_endpoints': api_urls}, status=200)

class TestAccount(APIView):
    permission_classes = [AllowAny]  # ✅ Open access for testing
    def get(self, request):
        return Response({"message": "This is a test endpoint for the Account app."}, status=status.HTTP_200_OK)
    
def privacy(request):
    return render(request, 'privacy.html')

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_account(request):
    request.user.delete()
    return Response({"message": "Account deleted successfully"}, status=200)


    