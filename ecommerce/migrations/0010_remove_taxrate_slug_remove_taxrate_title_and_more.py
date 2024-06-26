# Generated by Django 4.2.2 on 2024-03-31 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0009_alter_productsize_size_alter_productsize_size_label_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taxrate',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='taxrate',
            name='title',
        ),
        migrations.AlterField(
            model_name='productsize',
            name='size',
            field=models.CharField(blank=True, choices=[('m', 'M'), ('l', 'L'), ('xxs', 'XXS'), ('xxxl', 'XXXL'), ('xxl', 'XXL'), ('s', 'S'), ('xl', 'XL'), ('xxxs', 'XXXS'), ('xs', 'XS')], max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='productsize',
            name='size_label',
            field=models.CharField(blank=True, choices=[('in', 'Inches'), ('cm', 'CM'), ('ft', 'Feet')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.CharField(blank=True, choices=[('1', '1'), ('4', '4'), ('2', '2'), ('5', '5'), ('3', '3')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='status',
            field=models.CharField(blank=True, choices=[('draft', 'Draft'), ('published', 'Published')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='shippingsettings',
            name='shipping_status',
            field=models.CharField(blank=True, choices=[('delivered', 'Delivered'), ('shipped', 'Shipped'), ('preshipment', 'Pre-shipment'), ('unshipped', 'Unshipped')], max_length=50, null=True),
        ),
    ]
