# Generated by Django 5.0.4 on 2024-09-29 10:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_rename_additionalinfo_request_additional_info_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='requestinfo',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='request',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='requestinfo',
            name='user',
        ),
    ]
