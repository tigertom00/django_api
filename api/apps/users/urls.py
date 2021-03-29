from rest_framework import routers
from .views import UsersViewSet

router = routers.DefaultRouter()
router.register('', UsersViewSet, 'users')

urlpatterns = router.urls
