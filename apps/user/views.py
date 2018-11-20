# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from user import models
from user.models import UserInfo, UserGroup

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from user.serializers import UserInfoSerializer, UserGroupSerializer
from django.views import View
from django.http import JsonResponse


import time

class UserPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    page_query_param = "p"
    max_page_size = 100


class UserInfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserInfo.objects.all().order_by('id')
    serializer_class = UserInfoSerializer
    pagination_class = UserPagination


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


def login(request):
    if request.session.get('is_login', None):
        return redirect('dashboard')
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
                    # 记录最后登录时间
                    logintime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                    models.UserInfo.objects.filter(username=username).update(last_login_time=logintime)
                    return redirect('dashboard')
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
def dashboard(request):
    print("dashboard")
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/user/login?msg=你尚未登录,请登录后进行访问")
    return render(request, 'user/dashboard.html', locals())
