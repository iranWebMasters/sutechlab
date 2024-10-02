# Generated by Django 5.0.4 on 2024-10-02 10:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_sampleinfo_experiment'),
        ('services', '0026_sample_is_returnable'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TestInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repeat_count_test', models.PositiveIntegerField(verbose_name='تعداد تکرار آزمون')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ به\u200cروزرسانی')),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.experiment')),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.sample', verbose_name='شناسه نمونه آزمایش')),
                ('test', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.test', verbose_name='عنوان آزمایش')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
    ]
