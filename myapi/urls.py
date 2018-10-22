"""myapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.views.generic.base import RedirectView

import xadmin
from django.urls import path, include, re_path
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from rest_framework.documentation import include_docs_urls

# Create our schema's view w/ the get_schema_view() helper method. Pass in the proper Renderers for swagger
schema_view = get_schema_view(title='DEVOPS', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])


urlpatterns = [
    path('favicon.ico', serve, {'path': 'favicon.ico'}),
    # re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
    re_path(r'^swagger/', schema_view, name="DEVOPS"),
    re_path(r'^docs/', include_docs_urls(title="DEVOPS")),
    # re_path(r'^', include(router.urls)),            # restful api
    # re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),     # restful api
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('api/', include('mytable.urls')),
    path('user/', include('user.urls')),
    path('cmdb/', include('cmdb.urls')),
    path('ops/', include('ops.urls')),

]
