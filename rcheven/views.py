from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]  # Change to AllowAny if you want public access

class EventQueryView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        hn = request.data.get('HN')
        hn_year = request.data.get('HnYear')

        if not hn or not hn_year:
            return Response({"error": "HN and HnYear are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            events = Event.objects.filter(HN=hn, HnYear=hn_year)
            if not events.exists():
                return Response({"events": []}, status=status.HTTP_200_OK)

            serializer = EventSerializer(events, many=True)
            return Response({"events": serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TestRchEven(APIView):
    permission_classes = [AllowAny]  
    def get(self, request):
        return Response({"message": "This is a test endpoint for the RchData app."},status=status.HTTP_200_OK)
