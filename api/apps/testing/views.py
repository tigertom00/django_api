from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    # def get_queryset(self):
    #     return self.request.user.Post.all()

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)