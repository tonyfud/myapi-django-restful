# Create your views here.
from django.forms import model_to_dict
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse

from user import models
from user.models import UserInfo, UserGroup, Roles
from user.serializers import UserInfoSerializer, UserGroupSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.core import serializers
from django.core.paginator import Paginator
from django.db.models import Q

import django_filters

from django.views import View
from django.http import JsonResponse
from collections import OrderedDict

from rest_framework import filters

import time


class UserInfoFilter(django_filters.rest_framework.FilterSet):

    # 查询价格的范围
    # pricemin = django_filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    # pricemax = django_filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
    # 对商品名称进行模糊查询
    # name = django_filters.CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = UserInfo
        fields = ['username', 'email', 'realname', 'mobile', 'status']


class UserInfoPagination(PageNumberPagination):
    # page_size = 100
    # max_page_size = 100
    page_size_query_param = 'pageSize'
    page_query_param = "pageNumber"


class UserInfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    pagination_class = UserInfoPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_class = UserInfoFilter
    search_fields = ('username', 'realname', 'email', 'satus')
    ordering_fields = ('id', 'username', 'realname', 'email', 'satus' )

    # def get_queryset(self):
    #     queryset = Goods.objects.all()
    #     price_min = self.request.query_params.get("price_min", 0)
    #     if price_min:
    #         queryset = queryset.filter(shop_price__gt=price_min)
    #     return queryset

    def get_paginated_response(self, data):
        code = 200
        msg = 'success'
        if not data:
            code = 404
            msg = "data not found"

        return Response(OrderedDict([
            ('code', code),
            ('msg', msg),
            ('total', self._paginator.page.paginator.count),
            ('rows', data),
        ]))


class UserGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = UserGroup.objects.all().order_by('id')
    serializer_class = UserGroupSerializer


class json(View):
    def get(self, request, *args, **kwargs):
        result = {
            'status': True,
            'data': 'response data'
        }
        return JsonResponse(result, status=200)

    def post(self, request, *args, **kwargs):
        result = {
            'status': True,
            'data': 'response data'
        }
        return JsonResponse(result, status=200)


def info(request):
    return HttpResponse('{"code" : 20000, "data" : {"roles":["admin"],"name":"admin",'
                        '"avatar":"https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif"}}',
                        content_type="application/json")


def add(request):
    # ug_obj = models.UserGroup.objects.create(caption="外键数据添加")
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


def check_is_login(func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get("is_login"):
            return redirect("/user/login?msg=你尚未登录,请登录后进行访问")
        return func(request, *args, **kwargs)
    return wrapper


def check_is_login_api(func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get("is_login"):
            result = {
                'code': 401,
                'msg': '你尚未登录',
                'data': ''
            }
            return JsonResponse(result, status=200)
        return func(request, *args, **kwargs)
    return wrapper


def login(request):
    if request.session.get('is_login', None):
        return redirect('userlist')
    if request.method == "GET":
        msg = request.GET.get('msg', None)
        return render(request, 'user/login.html', {"message": msg})
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "所有字段都必须填写！"
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            try:
                user = models.UserInfo.objects.get(username=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    request.session['last_login_time'] = str(user.last_login_time)
                    # 记录最后登录时间
                    logintime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                    models.UserInfo.objects.filter(username=username).update(last_login_time=logintime)
                    return redirect('userlist')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'user/login.html', {"message": message})
    return render(request, 'user/login.html')
    # return HttpResponse('{"code" : 20000, "data" : {"token" : "admin"}}', content_type="application/json")


@check_is_login
def logout(request):
    # if not request.session.get('is_login', None):
    #     # 如果本来就未登录，也就没有登出一说
    #     return redirect("/user/login")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/user/login")
    # return HttpResponse('', content_type="application/json")


@check_is_login
def userlist(request):
    print("userlist")
    ret_data = dict()
    ret_data["showMoreQuery"] = "true"
    ret_data["canEdit"] = "true"
    ret_data["canDelete"] = "true"
    ret_data["activeSidebarUrl"] = request.path
    ret_data["APIUrl"] = "/user/get_user_list"

    return render(request, 'user/list.html', ret_data)


@check_is_login_api
def update_user_by_id(request):
    print("update_user_by_id")

    if request.method == "POST":
        print(request.POST)
        id = request.POST.get('id')
        username = request.POST.get('UserName')
        realname = request.POST.get('RealName')
        mobile = request.POST.get('Mobile')
        email = request.POST.get('Email')
        issupers = request.POST.get('IsSuper')
        status = request.POST.get('Status')
        password = request.POST.get('UserPwd')

        if id != '0':               # id 参数不等于 0 时为修改用户信息， 否则为新增用户
            if password is not '':  # 密码参数空时不修改密码
                ret = models.UserInfo.objects.filter(id=id).update(username=username,realname=realname,mobile=mobile,email=email,status=status,password=password)
            else:
                ret = models.UserInfo.objects.filter(id=id).update(username=username,realname=realname,mobile=mobile,email=email,status=status)

            if ret:                 # ret 有返回值时修改成功
                response_data = {'code': 0, 'msg': '用户信息修改成功 ID: ' + id, 'obj': id}
            else:
                response_data = {'code': 401, 'msg': '用户信息修改失败'}
        else:
            ret = models.UserInfo.objects.create(username=username,realname=realname,mobile=mobile,email=email,status=status,password=password)
            if ret:
                response_data = {'code': 0, 'msg': '用户新增成功 ID: ' + str(ret.id), 'obj': id}
            else:
                response_data = {'code': 401, 'msg': '用户新增失败'}

    return JsonResponse(response_data, safe=False)


@check_is_login_api
def get_user_list(request):
    print("get_user_list")

    if request.method == "GET":
        print(request.GET)
        pagesize = request.GET.get('pageSize')
        pagenumber = request.GET.get('pageNumber')
        sortname = request.GET.get('sortName')
        sortorder = request.GET.get('sortOrder')
        usernamelike = request.GET.get('usernamelike')
        realnamelike = request.GET.get('realnamelike')
        mobile = request.GET.get('mobile')
        status = request.GET.get('status')

    if usernamelike or realnamelike or mobile:                                  # 判断是否有搜索字

        q = Q()                                                                 # 创建Q对象，用于SQL查询 OR AND NOT ，以及动态字段
        if usernamelike:
            q.add(Q(**{'username__icontains': usernamelike}), Q.AND)
        if realnamelike:
            q.add(Q(**{'realname__icontains': realnamelike}), Q.AND)
        if mobile:
            q.add(Q(**{'mobile__icontains': mobile}), Q.AND)

        if sortname:                                                            # 判断是否有排序需求
            if sortname in ['id', 'username', 'realname', 'mobile', 'email']:   # 如果排序的列表在这些内容里面
                if sortorder == 'desc':                                         # 如果排序是反向
                    sortname = '-%s' % (sortname)
                all_records = models.UserInfo.objects.filter(q).order_by(sortname).values()
        else:
            all_records = models.UserInfo.objects.filter(q).values()
    else:
        if sortname:                                                            # 判断是否有排序需求
            if sortname in ['id', 'username', 'realname', 'mobile', 'email']:   # 如果排序的列表在这些内容里面
                if sortorder == 'desc':                                         # 如果排序是反向
                    sortname = '-%s' % (sortname)
                all_records = models.UserInfo.objects.all().order_by(sortname).values()
        else:
            all_records = models.UserInfo.objects.all().values()

    all_records_count = all_records.count()                                     # 统计数据总量，bootstarp-table 需要提供
    pageinator = Paginator(all_records, pagesize)                               # 开始做分页
    pageinator_records = pageinator.page(int(pagenumber))                       # 根据页码返回当前页数据
    model_dict = list(pageinator_records)                                       # 转换QuestSet数据为 list
    response_data = {'total': all_records_count, 'rows': model_dict}            # 必须带有rows和total这2个key，total表示总页数，rows表示每行的内容
    return JsonResponse(response_data, safe=False)                              # 返回JSON格式

@check_is_login
def edit_user_by_id(request):
    print("edit_user_by_id")

    if request.GET.get('id') == '0':    # ID 为0，表示为新增用户状态，否则为修改存在用户信息
        print('id=0')
        ret_data = dict()
        ret_data["id"] = '0'
        ret_data["UserName"] = ''
        ret_data["RealName"] = ''
        ret_data["Mobile"] = ''
        ret_data["Email"] = ''
        ret_data["Roles"] = ''
        ret_data["IsSuper"] = "false"
        ret_data["Status"] = ''
        render_page = 'user/add.html'
    else:
        user = models.UserInfo.objects.get(id=request.GET.get('id', None))
        print(user.username)
        ret_data = dict()
        ret_data["id"] = user.id
        ret_data["UserName"] = user.username
        ret_data["RealName"] = user.realname
        ret_data["Mobile"] = user.mobile
        ret_data["Email"] = user.email
        ret_data["Roles"] = user.group_id
        ret_data["IsSuper"] = "true"
        ret_data["Status"] = user.status
        render_page = 'user/edit.html'

    return render(request, render_page, ret_data)


@check_is_login_api
def get_roles_list(request):
    print("into get_roles_list")

    obj = models.Roles.objects.all().values()   # 'id', 'name', 'seq'
    #obj = models.Roles.objects.filter(name='超级管理员').values()

    model_dict = list(obj)
    print(model_dict)
    result = {
        'code': 0,
        'msg': "",
        'data': model_dict
    }

    return JsonResponse(result, safe=False)


@check_is_login_api
def batch_del_user_by_ids(request):
    print("batch_del_user_by_ids")
    ids = request.POST.get("ids")
    ids_dic = ids.split(',', -1)
    for id in ids_dic:
        print(id)
        ret = models.UserInfo.objects.filter(id=id).delete()
        if ret[0] == 1:
            code = 0
            msg = '删除用户成功'
        else:
            code = 404
            msg = '找不到用户信息'
            break

    result = {
        'code': code,
        'msg': msg,
        'data': '删除用户数据'
    }

    return JsonResponse(result, status=200)


@check_is_login
def menutree(request):
    print("menu-tree")
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/user/login?msg=你尚未登录,请登录后进行访问")

    resp = dict(code=0, msg="", obj=[{
        "Id": 35,
        "Name": "仪表板",
        "Parent": {
            "Id": 0,
            "Name": "",
            "Parent": "",
            "Rtype": 0,
            "Seq": 0,
            "Sons": "",
            "SonNum": 0,
            "Icon": "",
            "LinkUrl": "",
            "UrlFor": "",
            "HtmlDisabled": 0,
            "Level": 0,
            "RoleResourceRel": ""
        },
        "Rtype": 1,
        "Seq": 100,
        "Sons": "",
        "SonNum": 0,
        "Icon": "fa fa-chrome",
        "LinkUrl": "/user/dashboard",
        "UrlFor": "user.dashboard",
        "HtmlDisabled": 0,
        "Level": 0,
        "RoleResourceRel": ""
    }, {
        "Id": 8,
        "Name": "系统菜单",
        "Parent": {
            "Id": 0,
            "Name": "",
            "Parent": "",
            "Rtype": 0,
            "Seq": 0,
            "Sons": "",
            "SonNum": 0,
            "Icon": "",
            "LinkUrl": "",
            "UrlFor": "",
            "HtmlDisabled": 0,
            "Level": 0,
            "RoleResourceRel": ""
        },
        "Rtype": 0,
        "Seq": 200,
        "Sons": "",
        "SonNum": 2,
        "Icon": "",
        "LinkUrl": "",
        "UrlFor": "",
        "HtmlDisabled": 0,
        "Level": 0,
        "RoleResourceRel": ""
    },
        {
            "Id": 14,
            "Name": "系统管理",
            "Parent": {
                "Id": 8,
                "Name": "",
                "Parent": "",
                "Rtype": 0,
                "Seq": 0,
                "Sons": "",
                "SonNum": 0,
                "Icon": "",
                "LinkUrl": "",
                "UrlFor": "",
                "HtmlDisabled": 0,
                "Level": 0,
                "RoleResourceRel": ""
            },
            "Rtype": 1,
            "Seq": 90,
            "Sons": "",
            "SonNum": 2,
            "Icon": "fa fa-gears",
            "LinkUrl": "",
            "UrlFor": "",
            "HtmlDisabled": 0,
            "Level": 1,
            "RoleResourceRel": ""
        },
        {
            "Id": 23,
            "Name": "hosts",
            "Parent": {
                "Id": 14,
                "Name": "",
                "Parent": "",
                "Rtype": 0,
                "Seq": 0,
                "Sons": "",
                "SonNum": 0,
                "Icon": "",
                "LinkUrl": "",
                "UrlFor": "",
                "HtmlDisabled": 0,
                "Level": 0,
                "RoleResourceRel": ""
            },
            "Rtype": 1,
            "Seq": 100,
            "Sons": "",
            "SonNum": 0,
            "Icon": "",
            "LinkUrl": "/cmdb/hosts",
            "UrlFor": "cmdb.hosts",
            "HtmlDisabled": 0,
            "Level": 2,
            "RoleResourceRel": ""
        },
        {
            "Id": 36,
            "Name": "servers",
            "Parent": {
                "Id": 14,
                "Name": "",
                "Parent": "",
                "Rtype": 0,
                "Seq": 0,
                "Sons": "",
                "SonNum": 0,
                "Icon": "",
                "LinkUrl": "",
                "UrlFor": "",
                "HtmlDisabled": 0,
                "Level": 0,
                "RoleResourceRel": ""
            },
            "Rtype": 1,
            "Seq": 100,
            "Sons": "",
            "SonNum": 0,
            "Icon": "fa fa-book",
            "LinkUrl": "/cmdb/servers",
            "UrlFor": "cmdb.servers",
            "HtmlDisabled": 0,
            "Level": 2,
            "RoleResourceRel": ""
        }, {
            "Id": 7,
            "Name": "权限管理",
            "Parent": {
                "Id": 8,
                "Name": "",
                "Parent": "",
                "Rtype": 0,
                "Seq": 0,
                "Sons": "",
                "SonNum": 0,
                "Icon": "",
                "LinkUrl": "",
                "UrlFor": "",
                "HtmlDisabled": 0,
                "Level": 0,
                "RoleResourceRel": ""
            },
            "Rtype": 1,
            "Seq": 100,
            "Sons": "",
            "SonNum": 3,
            "Icon": "fa fa-balance-scale",
            "LinkUrl": "",
            "UrlFor": "",
            "HtmlDisabled": 0,
            "Level": 1,
            "RoleResourceRel": ""
        },
        {
            "Id": 9,
            "Name": "资源管理",
            "Parent": {
                "Id": 7,
                "Name": "",
                "Parent": "",
                "Rtype": 0,
                "Seq": 0,
                "Sons": "",
                "SonNum": 0,
                "Icon": "",
                "LinkUrl": "",
                "UrlFor": "",
                "HtmlDisabled": 0,
                "Level": 0,
                "RoleResourceRel": ""
            },
            "Rtype": 1,
            "Seq": 100,
            "Sons": "",
            "SonNum": 0,
            "Icon": "",
            "LinkUrl": "/resource/index",
            "UrlFor": "ResourceController.Index",
            "HtmlDisabled": 0,
            "Level": 2,
            "RoleResourceRel": ""
        }, {
            "Id": 12,
            "Name": "角色管理",
            "Parent": {
                "Id": 7,
                "Name": "",
                "Parent": "",
                "Rtype": 0,
                "Seq": 0,
                "Sons": "",
                "SonNum": 0,
                "Icon": "",
                "LinkUrl": "",
                "UrlFor": "",
                "HtmlDisabled": 0,
                "Level": 0,
                "RoleResourceRel": ""
            },
            "Rtype": 1,
            "Seq": 100,
            "Sons": "",
            "SonNum": 0,
            "Icon": "",
            "LinkUrl": "/role/index",
            "UrlFor": "RoleController.Index",
            "HtmlDisabled": 0,
            "Level": 2,
            "RoleResourceRel": ""
        },
        {
            "Id": 13,
            "Name": "用户管理",
            "Parent": {
                "Id": 7,
                "Name": "",
                "Parent": "",
                "Rtype": 0,
                "Seq": 0,
                "Sons": "",
                "SonNum": 0,
                "Icon": "",
                "LinkUrl": "",
                "UrlFor": "",
                "HtmlDisabled": 0,
                "Level": 0,
                "RoleResourceRel": ""
            },
            "Rtype": 1,
            "Seq": 100,
            "Sons": "",
            "SonNum": 0,
            "Icon": "",
            "LinkUrl": "/user/userlist",
            "UrlFor": "BackendUserController.Index",
            "HtmlDisabled": 0,
            "Level": 2,
            "RoleResourceRel": ""
        }
    ])
    return JsonResponse(resp)
