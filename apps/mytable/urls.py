#_*_coding:utf8_*_
from django.urls import path
from . import views

urlpatterns = [
    path('getLog', views.getLog, name='getLog'),
    path('singleCleanCache', views.singleCleanCache, name='singleCleanCache'),
    path('muiltCleanCache', views.muiltCleanCache, name='muiltCleanCache'),
]