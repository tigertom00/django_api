from rest_framework import routers
from .views import CharacterViewSet

router = routers.DefaultRouter()
router.register('', CharacterViewSet, 'character')

urlpatterns = router.urls
