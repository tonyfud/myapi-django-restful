# _*_coding:utf8_*_
from django.urls import path, re_path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()  # restful api
router.register(r'server', views.ServerViewSet)  # restful api

urlpatterns = [
    # re_path(r'^', include(router.urls)),
    path('GetHostList', views.GetHostList, name='GetHostList'),
    path('hosts', views.hosts_get_list, name='hosts_get_list'),
    path('servers', views.servers_get_list, name='servers_get_list'),
    # re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
