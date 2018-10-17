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

