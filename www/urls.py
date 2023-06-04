"""
URL configuration for www project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="home"),
    path("", include("django.contrib.auth.urls")),
    path("signup/", views.signup, name="signup"),
    path('polls/', include("pollsapp.urls")),
    path('theme/', include("themeapp.urls")),
    path("400/", views.test_400),
    path("403/", views.test_403),
    path("404/", views.test_404),
    path("500/", views.test_500),
    path("__reload__/", include("django_browser_reload.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler400 = 'www.views.error_400'
handler403 = 'www.views.error_403'
handler404 = 'www.views.error_404'
handler500 = 'www.views.error_500'
