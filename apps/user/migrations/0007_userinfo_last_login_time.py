# Generated by Django 2.1.2 on 2018-11-20 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20181019_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='last_login_time',
            field=models.DateTimeField(null=True, verbose_name='最后一次时间'),
        ),
    ]
