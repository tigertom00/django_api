from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from .views import BlacklistTokenView

schema = get_schema_view(title='DjangoAPI', description='API for all things...', version='1.0.0')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/blacklist/', BlacklistTokenView.as_view(), name='blacklist_token'),
    path('schema/', schema, name='schema'),
    path('docs/', include_docs_urls(title='DjangoAPI')),
]
