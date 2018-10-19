# Generated by Django 2.1 on 2018-10-17 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(db_index=True, max_length=32)),
                ('ip', models.GenericIPAddressField(db_index=True, protocol='ipv4')),
                ('port', models.IntegerField()),
                ('cpu', models.CharField(max_length=32, null=True)),
                ('mem', models.CharField(max_length=32, null=True)),
                ('type', models.CharField(max_length=32, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '主机总表',
                'verbose_name_plural': '主机总表',
            },
        ),
    ]