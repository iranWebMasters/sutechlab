# Generated by Django 4.2 on 2024-04-28 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_homepage_alter_contact_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'صفحه اصلی', 'verbose_name_plural': 'صفحه اصلی'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='top_text',
            field=models.TextField(default=1, verbose_name='متن بالای صفحه'),
            preserve_default=False,
        ),
    ]
