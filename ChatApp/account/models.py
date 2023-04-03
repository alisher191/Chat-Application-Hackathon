from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


class User(AbstractUser):
    username = None
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=12, unique=True)
    is_phone_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6)
    activation_code = models.CharField(max_length=40, blank=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.name

    def create_activation_code(self):
        import uuid
        code = str(uuid.uuid4())
        self.activation_code = code
