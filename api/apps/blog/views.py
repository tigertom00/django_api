from rest_framework import generics, viewsets, permissions
from .models import Blog
from .serializers import BlogSerializer

class BlogList(generics.ListCreateAPIView):
    pass

class BlogDetail(generics.RetrieveDestroyAPIView):
    pass

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

        