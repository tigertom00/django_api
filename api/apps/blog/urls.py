from rest_framework import routers
from django.urls import path
from .views import BlogList, BlogDetail, BlogViewSet, BlogListDetailfilter

router = routers.DefaultRouter()
router.register('viewset', BlogViewSet, 'blog')


urlpatterns = [
    path('', BlogList.as_view(), name='listcreate'),
    path('<str:pk>/', BlogDetail.as_view(), name='detailcreate'),
    path('search/custom/', BlogListDetailfilter.as_view, name='blogsearch')
]
urlpatterns += router.urls
