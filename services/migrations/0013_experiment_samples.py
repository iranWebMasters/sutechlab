# Generated by Django 5.0.4 on 2024-09-12 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0012_sample_standards_experiment_standards'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='samples',
            field=models.ManyToManyField(related_name='experiments', to='services.sample', verbose_name='نمونه\u200cها'),
        ),
    ]
