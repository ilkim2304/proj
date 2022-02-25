from .views import LoginAPIView, RegistrationAPIView
from django.urls import path

urlpatterns = [
    path("register", RegistrationAPIView.as_view(), name="Register"),
    path("login", LoginAPIView.as_view(), name="Login"),
]
