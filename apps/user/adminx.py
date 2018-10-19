import xadmin
from xadmin import views

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "MYAPI-后台"
    site_footer = "MYAPI"

# Register your models here.
from user.models import UserInfo, UserGroup, Business, VerifyCode, Token


class UserInfoAdmin(object):
    search_fields = ('username', 'email')
    list_editable = ('username', 'password', 'email', 'mobile', 'group', 'status')
    list_display = ('username', 'password', 'email', 'mobile', 'group', 'status', 'update_time')  # list
    list_filter = ('username', 'password', 'email', 'mobile', 'group', 'status', 'update_time')


class UserGroupAdmin(object):
    list_display = ('caption', 'create_date')  # list


class VerifyCodeAdmin(object):
    search_fields = ('mobile')
    list_display = ('mobile', 'code')  # list


class TokenAdmin(object):
    search_fields = ('user')
    list_display = ('user', 'token')  # list


xadmin.site.register(UserInfo, UserInfoAdmin)       #admin 后台编辑页，添加页只显示 UserInfo_Admin 定义的字段
xadmin.site.register(UserGroup, UserGroupAdmin)
xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(Token, TokenAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)