"""redproapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from django.urls import path
## login 
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include # new



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
  path("accounts/", include("django.contrib.auth.urls")),  # new
  path('probarranquilla/', views.probarranquilla, name='probarranquilla'),
    path('proantioquia/', views.proantioquia, name='proantioquia'),
    path('probogota/', views.probogota, name='probogota'),
    path('propacifico/', views.propacifico, name='propacifico'),
    path('prorisaralda/', views.prorisaralda, name='prorisaralda'),
    path('prosantamarta/', views.prosantamarta, name='prosantamarta'),
    path('prosantander/', views.prosantander, name='prosantander'),
    path('protolima/', views.protolima, name='protolima'),
    path('diauno/', views.diauno, name='diauno'),
path('userdata/', views.userdata, name='userdata'),
path('programa/', views.programa, name='programa'),
path('conprobarranquilla/', views.conprobarranquilla, name='conprobarranquilla'),
path('conproantioquia/', views.conproantioquia, name='conproantioquia'),
path('conprobogota/', views.conprobogota, name='conprobogota'),
path('conpropacifico/', views.conpropacifico, name='conpropacifico'),
path('conprorisaralda/', views.conprorisaralda, name='conprorisaralda'),
path('conprosantamarta/', views.conprosantamarta, name='conprosantamarta'),
path('conprosantander/', views.conprosantander, name='conprosantander'),
path('conprotolima/', views.conprotolima, name='conprotolima'),
path('diados/', views.diados, name='diados'),
path('compromiso/', views.compromiso, name='compromiso'),
path('comunicado/', views.comunicado, name='comunicado'),
path('lineamientos/', views.lineamientos, name='lineamientos'),

]