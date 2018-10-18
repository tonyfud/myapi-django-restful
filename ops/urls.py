#_*_coding:utf8_*_
from django.urls import path, re_path, include
from . import views

from rest_framework import routers


router = routers.DefaultRouter()                    # restful api
router.register(r'jobslist', views.JobsListViewSet)    # restful api

urlpatterns = [
    re_path(r'^', include(router.urls)),
]