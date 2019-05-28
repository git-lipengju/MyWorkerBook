"""hedge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from control_hedge import views
from django.contrib.staticfiles.urls import static
from hedge import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('control_hedge/index.html', views.index),
    path('control_hedge/login', views.login),
    path('control_hedge/cancel', views.cancel),
    path('control_hedge/start.html', views.start),
    path('control_hedge/to_start', views.to_start),
    path('control_hedge/to_stop', views.to_stop),
    path('control_hedge/', views.index),

]

urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
