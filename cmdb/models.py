from django.db import models


# Create your models here.


class Host(models.Model):
    """
    主机总表
    """
    hostname = models.CharField(max_length=32, db_index=True)
    ip = models.GenericIPAddressField(protocol='ipv4', db_index=True)
    port = models.IntegerField()
    cpu = models.CharField(max_length=32, null=True)
    mem = models.CharField(max_length=32, null=True)
    type = models.CharField(max_length=32, null=True)
    # business = models.ForeignKey(to='Business', to_field='id', on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, null=True, verbose_name="更新时间")  # 更新时自动更新时间

    class Meta:
        verbose_name = "主机总表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hostname


class Server(models.Model):
    """
    物理服务器
    """
    status_choice = (
        ('online', '上线'),
        ('offline', '下线'),
        ('normal', '正常'),
        ('abnormal', '异常')
    )

    server_name = models.CharField(verbose_name=u'服务器名称', max_length=128, blank=False, null=False)
    server_num = models.CharField(verbose_name=u'服务器编号', max_length=128, blank=True, null=True)
    brand = models.CharField(verbose_name=u'品牌', max_length=64, blank=True, null=True)
    model = models.CharField(verbose_name=u'型号', max_length=64, blank=True, null=True)
    cpus = models.IntegerField(verbose_name=u'cpu核数', default=0)
    ram = models.IntegerField(verbose_name=u'内存大小', default=0)
    disk = models.IntegerField(verbose_name=u'磁盘大小', default=0)
    product_date = models.DateTimeField(verbose_name=u'生产日期', auto_now_add=True)
    status = models.CharField(verbose_name=u'状态', max_length=16, choices=status_choice)

    create_date = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=u'修改时间', auto_now_add=True)

    class Meta:
        verbose_name = u'服务器'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.server_name
