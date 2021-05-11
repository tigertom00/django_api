from rest_framework import routers
from django.urls import path, re_path
from django.conf.urls import url
from .views import UsersViewSet, BlacklistTokenView, MyTokenObtainPairView, RefreshTokenView, TokenObtainPairView, TokenRefreshView, FileUploadView, UserUploadView

router = routers.DefaultRouter()
router.register('', UsersViewSet, 'users')
# router.register('logout/blacklist/', BlacklistTokenView, 'blacklist')

urlpatterns = router.urls + [
    path('logout/blacklist/', BlacklistTokenView.as_view(), name='blacklist'),
    path('token/refresh_token/', MyTokenObtainPairView.as_view(), name='refresh_token_only'),
    path('token/refresh/', RefreshTokenView.as_view(), name='refresh_token'),
    path('new/obtain/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('new/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('custom/upload/', UserUploadView.as_view(), name='upload_user'),
    # re_path(r'^upload_user/',FileUploadView.upload_user_profile),
    # url(r'^upload/$',FileUploadView.uploaduserprofile),
]
