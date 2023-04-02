from django.db import models
from django.contrib.auth.models import User


class Theme(models.Model): # Модель для темы комнаты
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model): # Модель для комнаты
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # Владелец комнаты
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True) # Участники комнаты
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model): # Модель для сообщений
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Отправитель
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # Комната, в которой было отправлено сообщение
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.first_name}: {self.content}'
    