from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, permissions, filters
from .models import Blog
from .serializers import BlogSerializer

#* Custom permission !only the author have write permit!

class BlogUserWritePermission(permissions.BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


#* Filter, Gets the blogs just for the current user

class BlogList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BlogSerializer

    def get_queryset(self):
        user = self.request.user
        return Blog.objects.filter(author=user)



class BlogDetail(generics.RetrieveUpdateDestroyAPIView, BlogUserWritePermission):
    permission_classes = [BlogUserWritePermission]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogListDetailfilter(generics.ListAPIView):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']

    # '^' Starts-with search.
    # '=' Exact matches.
    # '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
    # '$' Regex search.


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    # queryset = Blog.objects.all()
    permission_classes = [
        BlogUserWritePermission
    ]

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Blog, slug=item)

    def get_queryset(self):
        return Blog.objects.all()
    # def get_queryset(self):
    #     return self.queryset.filter(user=self.request.user)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

        