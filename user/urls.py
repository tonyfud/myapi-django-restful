#_*_coding:utf8_*_
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('info', views.info, name='info'),
    path('logout', views.logout, name='logout'),
    path('add', views.add, name='add'),
    path('getuserinfo', views.getuserinfo, name='getuserinfo'),
    path('getuserinfo2', views.getuserinfo2, name='getuserinfo2'),
]