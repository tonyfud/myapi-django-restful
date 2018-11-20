# Generated by Django 2.1.2 on 2018-10-19 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='business',
            options={'verbose_name': '工作组', 'verbose_name_plural': '工作组'},
        ),
        migrations.AlterModelOptions(
            name='usergroup',
            options={'verbose_name': '用户组', 'verbose_name_plural': '用户组'},
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '正常'), (1, '停用')], default=1, verbose_name='用户状态'),
        ),
    ]
