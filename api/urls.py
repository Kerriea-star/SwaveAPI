from django.urls import path
from .views import GenericUserAPIView, UserAPIView, CustomRegisterView

app_name = 'api'

urlpatterns = [
    path('users/', UserAPIView.as_view()),
    path('user/<int:id>/', GenericUserAPIView.as_view()),
    path('register/', CustomRegisterView.as_view()),
]