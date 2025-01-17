"""agile_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from attendance import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('attendance/', include('attendance.urls')),
#     path('', RedirectView.as_view(url='attendance/', permanent=False)),
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('attendance/', include('attendance.urls')),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]

urlpatterns += staticfiles_urlpatterns()