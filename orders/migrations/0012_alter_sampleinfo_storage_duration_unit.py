# Generated by Django 5.0.4 on 2024-09-30 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_alter_sampleinfo_sample_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sampleinfo',
            name='storage_duration_unit',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='واحد مدت زمان نگهداری'),
        ),
    ]
