# Generated by Django 5.0.4 on 2024-08-23 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_rename_banner_banners'),
    ]

    operations = [
        migrations.AddField(
            model_name='banners',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات بنر'),
        ),
    ]
