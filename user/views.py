# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from user import models
from user.models import UserInfo, UserGroup
from rest_framework import viewsets
from user.serializers import UserInfoSerializer, UserGroupSerializer


class UserInfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


class UserGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer


def login(request):
    return HttpResponse('{"code" : 20000, "data" : {"token" : "admin"}}', content_type="application/json")


def logout(request):
    return HttpResponse('', content_type="application/json")


def info(request):
    return HttpResponse('{"code" : 20000, "data" : {"roles":["admin"],"name":"admin","avatar":"https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif"}}', content_type="application/json")


def add(request):
    #ug_obj = models.UserGroup.objects.create(caption="外键数据添加")
    # 把外键ug_obj当参数传入
    models.UserInfo.objects.create(username='derek', password='123', group_id=1, email='derek@test.com', status=0)
    return HttpResponse('11')


def orm_add(request):
    models.UserInfo.objects.create(username='jack', passwd='456')
    return HttpResponse('22')


def orm_group(request):
    models.UserGroup.objects.create(caption='CEO')
    return HttpResponse('33')


def getuserinfo(request):
    obj = models.UserInfo.objects.all().first()
    print(obj.id, obj.username, obj.group_id, obj.group)
    return HttpResponse(str(obj.username) + ' / ' + str(obj.group))


def getuserinfo2(request):
    obj = models.UserInfo.objects.all().values('username')
    print(obj)
    return HttpResponse(obj)
