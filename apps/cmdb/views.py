from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Server, Host

from rest_framework import viewsets
from .serializers import ServerSerializer


class ServerViewSet(viewsets.ModelViewSet):
    """
    物理服务器视图
    """
    queryset = Server.objects.all().order_by('-create_date')
    serializer_class = ServerSerializer


def GetHostList(request):
    return HttpResponse('{"code" : 20000, "data" : {"token" : "admin"}}', content_type="application/json")