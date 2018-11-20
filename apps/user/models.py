from django.db import models


class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    create_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, null=True, verbose_name="更新时间")  # 更新时自动更新时间

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):  # 默认返回 code
        return self.code


class UserGroup(models.Model):
    """
    用户组表
    """
    caption = models.CharField(max_length=32, unique=True)  # 唯一索引
    create_date = models.DateTimeField(auto_now_add=True, null=True)  # 创建时生成时间
    update_time = models.DateTimeField(auto_now=True, null=True)  # 更新时自动更新时间

    class Meta:
        verbose_name = "用户组"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.caption


class UserInfo(models.Model):
    """
    用户信息表
    """
    username = models.CharField(max_length=32, unique=True, verbose_name="用户")
    password = models.CharField(max_length=64, verbose_name="密码")
    email = models.CharField(max_length=64, verbose_name="Email")
    mobile = models.CharField(max_length=11, verbose_name="电话号码")
    group = models.ForeignKey("UserGroup", to_field="id", default=1, on_delete=models.CASCADE,
                              verbose_name="用户组")  # 关联外键，生成字段名为user_group_id
    status_choices = ((0, '正常'), (1, '停用'))
    status = models.SmallIntegerField('用户状态', choices=status_choices, default=1)
    create_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, null=True, verbose_name="更新时间")  # 更新时自动更新时间
    last_login_time = models.DateTimeField(null=True, verbose_name="最后一次时间")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Token(models.Model):
    user = models.OneToOneField(to=UserInfo, on_delete=models.CASCADE)  # 一对一关系
    token = models.CharField(max_length=64)
    create_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, null=True, verbose_name="更新时间")  # 更新时自动更新时间


class Business(models.Model):
    """
    工作组表
    """
    caption = models.CharField(max_length=32, unique=True)
    code = models.CharField(max_length=32, null=True, default='QA')
    create_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, null=True, verbose_name="更新时间")  # 更新时自动更新时间

    class Meta:
        verbose_name = "工作组"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.caption
