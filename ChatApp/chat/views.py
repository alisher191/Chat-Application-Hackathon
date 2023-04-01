from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from .models import Room
from .serializers import RoomSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)


class RoomList(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    
class RoomDetailView(APIView):
    def get(self, request, pk):
        room = Room.objects.get(id=pk)
        serializer = RoomSerializer(room)
        return Response(serializer.data, status=status.HTTP_200_OK)
    