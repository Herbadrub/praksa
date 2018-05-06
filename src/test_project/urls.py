"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'test_project'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index_view, name="index"),
    #  url(r'^login_google/$', views.logingoogle_view, name="google"),
      url(r'^$', views.home),
    #  url(r'^login/$', views.login, name='login'),
    #  url(r'^logout/$', views.logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here
    url("^soc/", include("social_django.urls", namespace="social")),

    url(r'^accounts/', include('accounts.urls')),  # for accounts url

]
