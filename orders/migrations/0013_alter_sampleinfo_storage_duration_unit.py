# Generated by Django 5.0.4 on 2024-09-30 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_alter_sampleinfo_storage_duration_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sampleinfo',
            name='storage_duration_unit',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='واحد مدت زمان نگهداری'),
        ),
    ]
