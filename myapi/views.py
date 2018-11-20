# 添加以下代码
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required


def index(request):
    print("index")
    return render(request, 'index.html')