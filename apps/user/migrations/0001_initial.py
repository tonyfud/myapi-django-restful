# Generated by Django 2.1 on 2018-10-17 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32, unique=True)),
                ('code', models.CharField(default='QA', max_length=32, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '工作组表',
                'verbose_name_plural': '工作组表',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32, unique=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': '用户组表',
                'verbose_name_plural': '用户组表',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True, verbose_name='用户')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('email', models.CharField(max_length=64, verbose_name='Email')),
                ('mobile', models.CharField(max_length=11, verbose_name='电话号码')),
                ('status', models.SmallIntegerField(choices=[(0, '正常'), (1, '停用')], verbose_name='用户状态')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('group', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.UserGroup', verbose_name='用户组')),
            ],
            options={
                'verbose_name': '用户信息表',
                'verbose_name_plural': '用户信息表',
            },
        ),
        migrations.CreateModel(
            name='VerifyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='验证码')),
                ('mobile', models.CharField(max_length=11, verbose_name='电话')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '短信验证码',
                'verbose_name_plural': '短信验证码',
            },
        ),
    ]
