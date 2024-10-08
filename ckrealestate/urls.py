from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('realestate/', include('realestate.urls')),
    path('broker/', include('django.contrib.auth.urls')),
    path('broker/', include('broker.urls')),
    path('events/', include('events.urls')),
    path('reports/', include('reports.urls')),
    path('agent/', include('agent_profile.urls')),
    path('', include('realestate.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)