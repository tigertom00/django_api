from rest_framework import routers
from django.urls import path
from .views import BlogList, BlogDetail, BlogViewSet

router = routers.DefaultRouter()
router.register('viewset', BlogViewSet, 'blog')


urlpatterns = [
    path('', BlogList.as_view(), name='listcreate'),
    path('<int:pk>/', BlogDetail.as_view(), name='detailcreate'),
]
urlpatterns += router.urls
