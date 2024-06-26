# Generated by Django 4.2.2 on 2024-04-01 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0003_vendor_delete_vendorprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='vendor_email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendor',
            name='vendor_phone',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendor',
            name='vendor_website_URL',
            field=models.URLField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
