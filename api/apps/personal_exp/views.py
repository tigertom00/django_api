from rest_framework import viewsets, permissions
from .models import Character
from .serializers import CharacterSerializer


class CharacterViewSet(viewsets.ModelViewSet):

    serializer_class = CharacterSerializer
    queryset = Character.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
