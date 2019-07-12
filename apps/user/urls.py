#_*_coding:utf8_*_
from django.urls import path, re_path, include

from . import views

from rest_framework import routers

# restful api
router = routers.DefaultRouter()
router.register(r'users', views.UserInfoViewSet)
router.register(r'groups', views.UserGroupViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),            # restful api
    #page
    path('info', views.info, name='info'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('userlist', views.userlist, name='userlist'),
    # api
    path('menutree', views.menutree, name='menutree'),
    path('batch_del_user_by_ids', views.batch_del_user_by_ids, name='batch_del_user_by_ids'),
    path('edit_user_by_id', views.edit_user_by_id, name='edit_user_by_id'),
    path('get_roles_list', views.get_roles_list, name='get_roles_list'),
    path('get_user_list', views.get_user_list, name='get_user_list'),
    path('update_user_by_id', views.update_user_by_id, name='update_user_by_id'),

    # re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # path('login', views.login, name='login'),
    # path('info', views.info, name='info'),
    # path('logout', views.logout, name='logout'),
    # path('add', views.add, name='add'),
    # path('getuserinfo', views.getuserinfo, name='getuserinfo'),
    # path('getuserinfo2', views.getuserinfo2, name='getuserinfo2'),
]