from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.views.generic.base import RedirectView
from . import views # 添加
from django.contrib.auth import views as auth_views # 添加

import xadmin
from django.urls import path, include, re_path
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from rest_framework.documentation import include_docs_urls

# Create our schema's view w/ the get_schema_view() helper method. Pass in the proper Renderers for swagger
schema_view = get_schema_view(title='DEVOPS', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])


urlpatterns = [
    path('favicon.ico', serve, {'path': 'favicon.ico'}),

    # admin lte
    path('index/', views.index, name='index'),
    #
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
