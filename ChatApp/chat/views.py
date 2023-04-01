import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework import status
from asgiref.sync import async_to_sync

from .serializers import *


@api_view(['POST'])
def register(request):
    user_serializer = UserSerializer(data=request.data)
    profile_serializer = UserProfileSerializer(data=request.data)

    if user_serializer.is_valid() and profile_serializer.is_valid():
        user = user_serializer.save()
        user.set_password(user_serializer.validated_data['password'])
        user.save()

        profile = profile_serializer.save(user=user)

        # Send confirmation code to phone number here

        return Response({'message': 'User registered successfully'})

    return Response({'errors': user_serializer.errors + profile_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({'message': 'User logged in successfully'})

    return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['POST'])
def create_chat_room(request):
    serializer = ChatRoomSerializer(data=request.data)

    if serializer.is_valid():
        chat_room = serializer.save()
        chat_room.users.add(request.user)
        chat_room.save()

        return Response({'message': 'Chat room created successfully'})

    return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def join_chat_room(request):
    chat_room_id = request.data.get('chat_room_id')
    chat_room = ChatRoom.objects.get(id=chat_room_id)
    chat_room.users.add(request.user)

    return Response({'message': 'User joined chat room successfully'})


async def chat_message(self, event):
    message = event['message']
    await self.send(text_data=json.dumps(message))
