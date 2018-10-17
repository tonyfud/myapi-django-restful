from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def GetHostList(request):
    return HttpResponse('{"code" : 20000, "data" : {"token" : "admin"}}', content_type="application/json")