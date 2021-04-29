from rest_framework import routers
from django.urls import path
from .views import UsersViewSet, BlacklistTokenView, MyTokenObtainPairView, RefreshTokenView, TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('', UsersViewSet, 'users')
# router.register('logout/blacklist/', BlacklistTokenView, 'blacklist')

urlpatterns = router.urls + [
    path('logout/blacklist/', BlacklistTokenView.as_view(), name='blacklist'),
    path('token/refresh_token/', MyTokenObtainPairView.as_view(), name='refresh_token_only'),
    path('token/refresh/', RefreshTokenView.as_view(), name='refresh_token'),
    path('new/obtain/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('new/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
