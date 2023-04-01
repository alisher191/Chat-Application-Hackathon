from rest_framework.serializers import ModelSerializer, HiddenField, CurrentUserDefault, DateTimeField
from django.contrib.auth.models import User

from .models import Room


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class RoomSerializer(ModelSerializer):
    owner = HiddenField(default=CurrentUserDefault())
    created = DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated = DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model = Room
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['owner'] = UserSerializer(instance.owner).data['username']
        return ret
    