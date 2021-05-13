from rest_framework import generics, viewsets, permissions
from .models import Blog
from .serializers import BlogSerializer


class BlogUserWritePermission(permissions.BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user



class BlogList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Blog.postobjects.all()
    serializer_class = BlogSerializer

class BlogDetail(generics.RetrieveUpdateDestroyAPIView, BlogUserWritePermission):
    permission_classes = [BlogUserWritePermission]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    # def get_queryset(self):
    #     return self.queryset
    # def get_queryset(self):
    #     return self.queryset.filter(user=self.request.user)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

        