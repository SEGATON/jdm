# Generated by Django 4.2.2 on 2024-04-02 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0021_alter_productsize_size_alter_productsize_size_label_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_products',
            field=models.ManyToManyField(blank=True, null=True, related_name='brand_products', to='ecommerce.product'),
        ),
        migrations.AlterField(
            model_name='productsize',
            name='size',
            field=models.CharField(blank=True, choices=[('m', 'M'), ('xl', 'XL'), ('xs', 'XS'), ('xxxs', 'XXXS'), ('s', 'S'), ('xxl', 'XXL'), ('xxxl', 'XXXL'), ('l', 'L'), ('xxs', 'XXS')], max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='productsize',
            name='size_label',
            field=models.CharField(blank=True, choices=[('ft', 'Feet'), ('in', 'Inches'), ('cm', 'CM')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.CharField(blank=True, choices=[('1', '1'), ('5', '5'), ('2', '2'), ('4', '4'), ('3', '3')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='status',
            field=models.CharField(blank=True, choices=[('draft', 'Draft'), ('published', 'Published')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='shippingsettings',
            name='shipping_status',
            field=models.CharField(blank=True, choices=[('preshipment', 'Pre-shipment'), ('unshipped', 'Unshipped'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='shippingsettings',
            name='shipping_type',
            field=models.CharField(blank=True, choices=[('free_express_shipping', 'Free Express Shipping'), ('free_2_day_shipping', 'Free 2 Day Shipping'), ('free_shipping', 'Free Shipping')], max_length=70, null=True),
        ),
    ]