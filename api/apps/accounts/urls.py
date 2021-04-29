from django.urls import path, include
from rest_framework.authtoken import views
from .views import RegisterAPI, LoginAPI, UserAPI

urlpatterns = [
    path('', views.obtain_auth_token),
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('user/', UserAPI.as_view()),
    ]
