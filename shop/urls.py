from django.apps import apps
from django.urls import include, path 
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('i18n/', include('django.conf.urls.i18n')), 
    path('admin/', admin.site.urls), 
    path('', include(apps.get_app_config('oscar').urls[0])),
    path('api-auth/', include('rest_framework.urls')),
    path("api/", include("oscarapi.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
