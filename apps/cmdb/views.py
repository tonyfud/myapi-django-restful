from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Server, Host

from rest_framework import viewsets
from .serializers import ServerSerializer

from django.shortcuts import render
from django.shortcuts import redirect

from apps.user.views import check_is_login


class ServerViewSet(viewsets.ModelViewSet):
    """
    物理服务器视图
    """
    queryset = Server.objects.all().order_by('-create_date')
    serializer_class = ServerSerializer


def GetHostList(request):
    return HttpResponse('{"code" : 20000, "data" : {"token" : "admin"}}', content_type="application/json")


@check_is_login
def hosts_get_list(request):
    # if not request.session.get('is_login', None):
    #     # 如果本来就未登录，也就没有登出一说
    #     return redirect("/user/login?msg=你尚未登录,请登录后进行访问")
    hosts = Host.objects.all()
    return render(request, 'cmdb/hosts_list.html', {"hosts": hosts})


@check_is_login
def servers_get_list(request):
    # if not request.session.get('is_login', None):
    #     # 如果本来就未登录，也就没有登出一说
    #     return redirect("/user/login?msg=你尚未登录,请登录后进行访问")
    servers = Server.objects.all()
    return render(request, 'cmdb/servers_list.html', {"servers": servers})
