from django.db import models

# Create your models here.


class JobsList(models.Model):
    """
    任务列表
    """
    create_date = models.DateTimeField(auto_now_add=True, null=True)  # 创建时生成时间
    user = models.CharField(max_length=32, verbose_name="创建人")
    action = models.CharField(max_length=32, verbose_name="动作")
    info = models.CharField(max_length=32, verbose_name="信息")
    parameter = models.CharField(max_length=32, verbose_name="参数")
    status = models.CharField(max_length=32, verbose_name="状态")
    update_time = models.DateTimeField(auto_now=True, null=True, verbose_name="更新时间")  # 更新时自动更新时间

    class Meta:
        verbose_name = "任务列表"
        verbose_name_plural = verbose_name

    def __str__(self):  # 默认返回 info
        return self.info