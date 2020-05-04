"""locallibrary URL Configuration

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
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
]

# Use include() to add URLs from the application directory
urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
     path('catalog/', include('catalog.urls')),
]

# Use static () to add ratios for static files
# Only for the development period
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Add a ratio URL to redirect requests from the root URL to the application URL
urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]