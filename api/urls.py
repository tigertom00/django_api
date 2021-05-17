from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from dj_rest_auth.registration.views import VerifyEmailView

from .views import FacebookLogin
# from api.settings.base import BASE_DIR
# from api.settings.dev import VENV_PATH
# import sys
# print(BASE_DIR, file=sys.stderr)
# print(VENV_PATH, file=sys.stderr)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('dj-rest-auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('allauth/', include('allauth.urls')),
    
    
    path('home/', include('api.apps.home.urls')),
    path('api/users/', include('api.apps.users.urls')),
    # path('api/accounts/', include('api.apps.accounts.urls')),
    path('api/todo/', include('api.apps.todo.urls')),
    path('api/blog/', include('api.apps.blog.urls')),
    path('api/utils/', include('api.apps.utils.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
        path('api/testing/', include('api.apps.testing.urls')),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        
    
