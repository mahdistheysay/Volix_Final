"""
URL configuration for VolixTest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from VolixTest import settings
from VolixTest.views import home_page , header , footer , contact_us_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page , name = 'home'),
    path('header', header , name='header'),
    path('footer', footer , name='footer'),
    path('contact-us', contact_us_page , name='contact'),

]


if settings.DEBUG :
       urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
       urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
