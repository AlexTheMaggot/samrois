# DjangoImports
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
# End DjangoImports

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
]

handler404 = 'mainapp.views.custom_404'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
