# Generated by Django 5.0.4 on 2024-10-06 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_testinformation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sampleinfo',
            name='sample_unit',
        ),
    ]
