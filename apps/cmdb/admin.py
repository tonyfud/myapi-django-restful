from django.contrib import admin
from cmdb.models import Host, Server

# Register your models here.


class ServerAdmin(admin.ModelAdmin):
    search_fields = ('username', 'email')
    list_display = ('server_name', 'server_num')  # list


admin.site.register(Server, ServerAdmin)
admin.site.register([Host, ])
