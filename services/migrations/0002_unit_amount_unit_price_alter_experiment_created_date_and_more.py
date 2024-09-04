# Generated by Django 5.0.4 on 2024-09-04 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_image'),
        ('devices', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit_amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50, verbose_name='مقدار')),
                ('unit', models.CharField(choices=[('C', 'سانتی گراد'), ('F', 'فارنهایت'), ('K', 'کلوین'), ('H', 'ساعت'), ('MIN', 'دقیقه'), ('S', 'ثانیه')], max_length=50, verbose_name='واحد اندازه\u200cگیری')),
            ],
        ),
        migrations.CreateModel(
            name='Unit_price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=0, max_digits=15, verbose_name='مبلغ واحد')),
                ('currency', models.CharField(choices=[('IRR', 'ریال'), ('Toman', 'تومان')], default='IRR', max_length=5, verbose_name='واحد پول')),
            ],
        ),
        migrations.AlterField(
            model_name='experiment',
            name='created_date',
            field=models.DateField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='description',
            field=models.TextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiments', to='devices.device', verbose_name='دستگاه'),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiments', to='services.faculty', verbose_name='دانشکده'),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='laboratory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiments', to='services.laboratory', verbose_name='آزمایشگاه'),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiments', to='accounts.profile', verbose_name='اپراتور'),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='status',
            field=models.CharField(choices=[('active', 'فعال'), ('inactive', 'غیرفعال')], default='active', max_length=8, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='title',
            field=models.CharField(max_length=255, verbose_name='عنوان آزمایش'),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='updated_date',
            field=models.DateField(auto_now=True, verbose_name='تاریخ به\u200cروزرسانی'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='location',
            field=models.CharField(choices=[('SD', 'صدرا'), ('SH', 'شیراز')], max_length=2, verbose_name='مکان'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='name',
            field=models.CharField(max_length=255, verbose_name='نام دانشکده'),
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='location',
            field=models.CharField(choices=[('SD', 'صدرا'), ('SH', 'شیراز')], max_length=2, verbose_name='مکان'),
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='name',
            field=models.CharField(max_length=255, verbose_name='نام آزمایشگاه'),
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام پارامتر')),
                ('unit', models.CharField(choices=[('C', 'سانتی گراد'), ('F', 'فارنهایت'), ('K', 'کلوین'), ('H', 'ساعت'), ('MIN', 'دقیقه'), ('S', 'ثانیه')], max_length=50, verbose_name='واحد اندازه\u200cگیری')),
                ('laboratory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='services.laboratory', verbose_name='آزمایشگاه')),
                ('unit_amount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameters', to='services.unit_amount', verbose_name='مقدار واحد')),
                ('unit_price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameters', to='services.unit_price', verbose_name='مبلغ واحد')),
            ],
        ),
    ]
