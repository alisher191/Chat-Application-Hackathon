from rest_framework.serializers import ModelSerializer, HiddenField, CurrentUserDefault, DateTimeField
from django.contrib.auth.models import User

from .models import Room


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class RoomSerializer(ModelSerializer):
    owner = HiddenField(default=CurrentUserDefault())
    created = DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True) # read_only=True - поля только для чтения
    updated = DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True) # Эти поля будут автоматически заполнены при создании или обновлении объекта, но они не будут доступны для редактирования пользователем.
    class Meta:
        model = Room
        fields = '__all__' # все поля в модели комнаты будут сериализованы.

    def to_representation(self, instance): # переопределяем метод "to_representation"
        ret = super().to_representation(instance) # Цель этого метода — изменить сериализованные данные для объекта экземпляра перед его возвратом
        ret['owner'] = UserSerializer(instance.owner).data['username'] # Вместо id владельца будет возвращён его username
        return ret
    