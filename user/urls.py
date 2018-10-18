#_*_coding:utf8_*_
from django.urls import path, re_path, include
from . import views

from rest_framework import routers


router = routers.DefaultRouter()                    # restful api
router.register(r'users', views.UserInfoViewSet)    # restful api
router.register(r'groups', views.UserGroupViewSet)  # restful api

urlpatterns = [
    re_path(r'^', include(router.urls)),
    # path('login', views.login, name='login'),
    # path('info', views.info, name='info'),
    # path('logout', views.logout, name='logout'),
    # path('add', views.add, name='add'),
    # path('getuserinfo', views.getuserinfo, name='getuserinfo'),
    # path('getuserinfo2', views.getuserinfo2, name='getuserinfo2'),
]