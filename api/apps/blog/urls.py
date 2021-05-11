from rest_framework import routers
from django.urls import path
from .views import BlogList, BlogDetail, BlogViewSet

router = routers.DefaultRouter()
router.register('', BlogViewSet, 'blog')

urlpatterns = router.urls

# urlpatterns += [
#     path('testing/<int:pk>/', BlogDetail.as_view(), name='detailcreate'),
#     path('testing/', BlogList.as_view(), name='listcreate')
# ]
