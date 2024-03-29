# Generated by Django 2.1.2 on 2018-10-18 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_name', models.CharField(max_length=128, verbose_name='服务器名称')),
                ('server_num', models.CharField(blank=True, max_length=128, null=True, verbose_name='服务器编号')),
                ('brand', models.CharField(blank=True, max_length=64, null=True, verbose_name='品牌')),
                ('model', models.CharField(blank=True, max_length=64, null=True, verbose_name='型号')),
                ('cpus', models.IntegerField(default=0, verbose_name='cpu核数')),
                ('ram', models.IntegerField(default=0, verbose_name='内存大小')),
                ('disk', models.IntegerField(default=0, verbose_name='磁盘大小')),
                ('product_date', models.DateTimeField(auto_now_add=True, verbose_name='生产日期')),
                ('status', models.CharField(choices=[('online', '上线'), ('offline', '下线'), ('normal', '正常'), ('abnormal', '异常')], max_length=16, verbose_name='状态')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '服务器',
                'verbose_name_plural': '服务器',
            },
        ),
    ]
