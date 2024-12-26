from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static

from kve import settings
from databank.views.home import home_page
from databank.views.lang import lang_page
from databank.views.family import family_page
from databank.views.genus import genus_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('lang/', lang_page),
    path('family/', family_page),
    path('genus/', genus_page),
    path('', home_page), 
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
