from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from .models import Room
from .serializers import RoomSerializer


@api_view(['GET'])
def getRoutes(request):
    """Возвращает эндпоинты наших API"""
    routes = [
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)


class RoomList(generics.ListAPIView):
    queryset = Room.objects.all() # список объектов, которые должны быть возвращены представлением
    serializer_class = RoomSerializer # класс сериализатора, используемый для сериализации данных, возвращаемых представлением

    
class RoomDetailView(APIView):
    def get(self, request, pk): # обрабатывает запросы GET для получения определенного объекта Room по его первичному ключу (pk)
        room = Room.objects.get(id=pk) # список объектов, которые должны быть возвращены представлением
        serializer = RoomSerializer(room) # класс сериализатора, используемый для сериализации данных, возвращаемых представлением
        return Response(serializer.data, status=status.HTTP_200_OK)
    