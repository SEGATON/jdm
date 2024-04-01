# Generated by Django 4.2.2 on 2024-03-31 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0015_alter_productsize_size_alter_productsize_size_label_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsize',
            name='size',
            field=models.CharField(blank=True, choices=[('xxs', 'XXS'), ('s', 'S'), ('m', 'M'), ('l', 'L'), ('xxl', 'XXL'), ('xxxs', 'XXXS'), ('xs', 'XS'), ('xl', 'XL'), ('xxxl', 'XXXL')], max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='productsize',
            name='size_label',
            field=models.CharField(blank=True, choices=[('cm', 'CM'), ('ft', 'Feet'), ('in', 'Inches')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.CharField(blank=True, choices=[('3', '3'), ('4', '4'), ('5', '5'), ('1', '1'), ('2', '2')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='shippingsettings',
            name='shipping_status',
            field=models.CharField(blank=True, choices=[('shipped', 'Shipped'), ('preshipment', 'Pre-shipment'), ('delivered', 'Delivered'), ('unshipped', 'Unshipped')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='shippingsettings',
            name='shipping_type',
            field=models.CharField(blank=True, choices=[('free_2_day_shipping', 'Free 2 Day Shipping'), ('free_shipping', 'Free Shipping'), ('free_express_shipping', 'Free Express Shipping')], max_length=70, null=True),
        ),
    ]
