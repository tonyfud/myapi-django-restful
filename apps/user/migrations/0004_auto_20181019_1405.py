# Generated by Django 2.1.2 on 2018-10-19 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='username',
            new_name='user',
        ),
    ]
