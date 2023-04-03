from django.contrib import messages
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .form import MyForm
from .helpers import send_otp_to_phone
from .models import User
from .serializers import ChangePasswordSerializer, ForgotPasswordSerializer, ForgotPasswordCompleteSerializer


@api_view(['POST'])
def send_otp(request):
    data = request.data

    if data.get('phone_number') is None:
        return Response({
            'ststus': 400,
            'message': 'key phone_number is required'
        })

    if data.get('email') is None:
        return Response({
            'ststus': 400,
            'message': 'key email is required'
        })

    if data.get('password') is None:
        return Response({
            'ststus': 400,
            'message': 'key password is required'
        })

    user = User.objects.create(phone_number=data.get('phone_number'), otp=send_otp_to_phone(data.get('phone_number')),
                               name=data.get('name'), email=data.get('email'))
    user.set_password = data.get('set_password')
    user.save()

    return Response({
        'ststus': 200,
        'message': 'Otp Sent'
    })


@api_view(['POST'])
def verify_otp(request):
    data = request.data

    if data.get('phone_number') is None:
        return Response({
            'ststus': 400,
            'message': 'key phone_number is required'
        })

    if data.get('name') is None:
        return Response({
            'ststus': 400,
            'message': 'key name is required'
        })

    if data.get('otp') is None:
        return Response({
            'ststus': 400,
            'message': 'key otp is required'
        })

    try:
        user_obj = User.objects.get(phone_number=data.get('phone_number'))

    except Exception:
        return Response({
            'ststus': 400,
            'message': 'invalid phone'
        })

    if user_obj.otp == data.get('otp'):
        user_obj.is_phone_verified = True
        user_obj.save()
        return Response({
            'status': 200,
            'message': 'otp matched'
        })

    return Response({
        'status': 200,
        'message': 'invalid otp'
    })


def home(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Success')
        else:
            messages.error(request, 'Wrong captcha')
    form = MyForm
    return render(request, 'home.html', {'form': form})


class ChangePasswordApiView(APIView):

    @staticmethod
    def post(request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('Вы успешно изменили свой пароль')


class ForgotPasswordApiView(APIView):
    @staticmethod
    def post(request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        return Response('Вам отправлено письмо для восстановления пароля')


class ForgotPasswordCompleteApiView(APIView):
    @staticmethod
    def post(request):
        serializer = ForgotPasswordCompleteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('Пароль успешно обновлен')
