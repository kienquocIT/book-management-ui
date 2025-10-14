"""
URL configuration for ui project.

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
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from ui import settings


def cached_serve(request, path, document_root=None):
    response = serve(request, path, document_root)
    # Thêm caching headers
    response["Cache-Control"] = "max-age=31536000, public, immutable"
    return response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('book/', include('book.urls')),
    path('author/', include('author.urls')),
    path('', include('authentication.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', cached_serve, {'document_root': settings.MEDIA_ROOT}),
    ]
