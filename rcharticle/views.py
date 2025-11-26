from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.permissions import AllowAny

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        """
        Returns the appropriate permissions based on the method or action.
        """
        if self.action == 'list':
            return [IsAuthenticated()]  # Anyone can view articles
        elif self.action == 'create':
            return [IsAdminUser()]  # Only authenticated users can create
        elif self.action == 'destroy':
            return [IsAdminUser()]  # Only authenticated users can soft delete
        elif self.action == 'hard_delete':
            return [IsAdminUser()]  # Only authenticated users can hard delete
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        """
        Handles listing all Articles.
        """
        queryset = Article.active_objects.all()  # Use the custom manager to exclude soft-deleted items
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        """
        Handles soft deletion of an Article.
        """
        instance = self.get_object()
        instance.Is_Delete = True  # Perform soft deletion
        instance.save()
        return Response({"message": "Article soft-deleted successfully."}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def hard_delete(self, request, pk=None):
        """
        Handles hard deletion of an Article.
        """
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Article hard-deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
class TestRcharticle(APIView):
    permission_classes = [AllowAny]  # ✅ Open access for testing
    def get(self, request):
        return Response({"message": "This is a test endpoint for the RchArticle app."}, status=status.HTTP_200_OK)