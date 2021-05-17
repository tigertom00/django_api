from rest_framework import viewsets, permissions, mixins, status, generics
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenViewBase
from .serializers import UsersSerializer, MyTokenObtainPairSerializer, TokenObtainLifetimeSerializer, TokenRefreshLifetimeSerializer
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import CustomUser

User = get_user_model()


class UsersViewSet(viewsets.ModelViewSet):

    serializer_class = UsersSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    queryset = User.objects.all()

    def get_queryset(self):

        return self.queryset.filter(username=self.request.user)

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)
