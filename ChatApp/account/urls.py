from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('', home, name='home'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('send_otp/', send_otp),
    path('verify_otp/', verify_otp),
    path('forgot_password/', ForgotPasswordApiView.as_view()),
    path('forgot_password_complete/', ForgotPasswordCompleteApiView.as_view()),
    path('change_password/', ChangePasswordApiView.as_view())
]
