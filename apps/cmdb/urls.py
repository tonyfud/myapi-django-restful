# _*_coding:utf8_*_
from django.urls import path, re_path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()  # restful api
router.register(r'server', views.ServerViewSet)  # restful api

urlpatterns = [
    re_path(r'^', include(router.urls)),
    path('GetHostList', views.GetHostList, name='GetHostList'),
    # re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
