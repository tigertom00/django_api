from django.urls import path
from .views import BlacklistTokenView

urlpatterns = [
    path('blacklist/', BlacklistTokenView.as_view(), name='blacklist_token'),
]
