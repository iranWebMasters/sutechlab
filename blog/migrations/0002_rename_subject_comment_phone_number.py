# Generated by Django 4.2 on 2024-05-01 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='subject',
            new_name='phone_number',
        ),
    ]
