"""
URL configuration for kve project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from databank.views.home import home_page
from databank.views.lang import lang_page
from databank.views.family import family_page
from databank.views.genus import genus_page

from databank.views.post_main_comment import main_comment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lang/', lang_page),
    path('family/', family_page),
    path('genus/', genus_page),
    path('', home_page), 

    path('post_main_comment/', main_comment),
]
