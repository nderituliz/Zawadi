from django.conf.urls import url, include
from django.urls import path, include
# from . import views
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('rateme.urls')),
    path('accounts/', include('rateme.urls')),
    url('accounts/', include('django.contrib.auth.urls')),
    # url(r'^logout/$', views.logout, {"next_page": '/accounts/login/'}),
    url(r'^api/', include('rateme.api.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)