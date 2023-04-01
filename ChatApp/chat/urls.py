from django.urls import path
from .views import UserList, UserDetail, ChatRoomList, ChatRoomDetail, MessageList, MessageDetail

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('chatrooms/', ChatRoomList.as_view()),
    path('chatrooms/<int:pk>/', ChatRoomDetail.as_view()),
    path('messages/', MessageList.as_view()),
    path('messages/<int:pk>/', MessageDetail.as_view()),
]
