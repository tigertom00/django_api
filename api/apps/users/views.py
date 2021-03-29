from rest_framework import viewsets, permissions
from .serializers import UsersSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UsersViewSet(viewsets.ModelViewSet):

    serializer_class = UsersSerializer
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
