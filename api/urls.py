from django.contrib import admin
from django.conf import settings
from django.urls import path, include


from api.settings.base import BASE_DIR
from api.settings.dev import VENV_PATH
import sys
print(BASE_DIR, file=sys.stderr)
print(VENV_PATH, file=sys.stderr)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('home/', include('api.apps.home.urls')),
    path('api/users/', include('api.apps.users.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
        path('api/testing/', include('api.apps.testing.urls')),
    ]
