from django.urls import path

from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('rooms/', views.RoomList.as_view()),
    path('rooms/<int:pk>/', views.RoomDetailView.as_view()),
]
