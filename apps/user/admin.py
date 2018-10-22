from django.contrib import admin

# Register your models here.
from .models import UserInfo, UserGroup, Business, VerifyCode


# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    fields = ('username', 'password')  # 只显示 两个字段 username 和 password


class UserInfoAdmin2(admin.ModelAdmin):
    search_fields = ('username', 'email')
    list_display = ('username', 'password', 'email', 'mobile', 'group', 'status', 'update_time')  # list
    fieldsets = (
        ['基本信息', {
            'fields': ('username', 'password'),
        }],
        ['更多信息', {
            'classes': ('collapse',),  # CSS
            'fields': ('email', 'mobile', 'group', 'status'),
        }]
    )


admin.site.register(UserInfo, UserInfoAdmin2)  # admin 后台编辑页，添加页只显示 UserInfo_Admin 定义的字段
admin.site.register([UserGroup, Business, VerifyCode])