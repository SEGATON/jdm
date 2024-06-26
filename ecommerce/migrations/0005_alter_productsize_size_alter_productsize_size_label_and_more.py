# Generated by Django 4.2.2 on 2024-03-20 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_productmetas_author_alter_productsize_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsize',
            name='size',
            field=models.CharField(blank=True, choices=[('xl', 'XL'), ('xxl', 'XXL'), ('m', 'M'), ('xxxs', 'XXXS'), ('s', 'S'), ('l', 'L'), ('xs', 'XS'), ('xxs', 'XXS'), ('xxxl', 'XXXL')], max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='productsize',
            name='size_label',
            field=models.CharField(blank=True, choices=[('cm', 'CM'), ('in', 'Inches'), ('ft', 'Feet')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.CharField(blank=True, choices=[('2', '2'), ('1', '1'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='shippingsettings',
            name='shipping_status',
            field=models.CharField(blank=True, choices=[('delivered', 'Delivered'), ('preshipment', 'Pre-shipment'), ('unshipped', 'Unshipped'), ('shipped', 'Shipped')], max_length=50, null=True),
        ),
    ]
