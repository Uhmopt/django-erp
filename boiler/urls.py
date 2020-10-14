"""boiler URL Configuration

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
from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from users import views as user_view
from zonemonitor import views as zone_monitor_view
from zoneexplore import views as zone_explore_view
from boilermonitor import views as boiler_monitor_view
from boilerexplore import views as boiler_explore_view
from maintanancemonitor import views as maintanance_monitor_view
from maintananceexplore import views as maintanance_explore_view
from wheathermonitor import views as wheather_monitor_view
from wheatherexplore import views as wheather_explore_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('zone_monitor/<int:zone_id>/', zone_monitor_view.viewTemplate, name='zone_monitor'),
    path('zone_explore/<int:zone_id>/', zone_explore_view.viewTemplate, name='zone_explore'),
    path('boiler_monitor/', boiler_monitor_view.viewTemplate, name='boiler_monitor'),
    path('boiler_explore/', boiler_explore_view.viewTemplate, name='boiler_explore'),
    path('maintanance_monitor/', maintanance_monitor_view.viewTemplate, name='maintanance_monitor'),
    path('maintanance_explore/', maintanance_explore_view.viewTemplate, name='maintanance_explore'),
    path('wheather_monitor/', wheather_monitor_view.viewTemplate, name='wheather_monitor'),
    path('wheather_explore/', wheather_explore_view.viewTemplate, name='wheather_explore'),
    path('', RedirectView.as_view(url='zone_monitor/1/', permanent=True)),
]
