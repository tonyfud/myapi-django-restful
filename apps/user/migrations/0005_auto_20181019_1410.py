# Generated by Django 2.1.2 on 2018-10-19 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20181019_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='token',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间'),
        ),
    ]
