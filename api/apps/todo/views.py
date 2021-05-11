from rest_framework import viewsets, permissions
from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)