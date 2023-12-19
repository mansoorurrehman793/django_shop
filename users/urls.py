from django.urls import path, include
from users.views import LoginView, SignUpView
from . import views


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    # path('register/',UserRegistrationView.as_view(),name="register"),
    path("signup/", SignUpView.as_view(), name="sign-up"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("login/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("email-exsist/", views.CheckEmailExistsView.as_view(), name="email-exsist"),
    path("email-verify/", views.VerifyEmail.as_view(), name="email-verify"),
    # path('profile/', UserProfileView.as_view(), name='profile'),
    # path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    # path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    # path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
]
