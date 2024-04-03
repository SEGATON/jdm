# Generated by Django 4.2.2 on 2024-04-03 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce', '0024_product_vote_alter_productsize_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsize',
            name='size',
            field=models.CharField(blank=True, choices=[('xl', 'XL'), ('m', 'M'), ('xxxl', 'XXXL'), ('xs', 'XS'), ('s', 'S'), ('l', 'L'), ('xxl', 'XXL'), ('xxs', 'XXS'), ('xxxs', 'XXXS')], max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='productsize',
            name='size_label',
            field=models.CharField(blank=True, choices=[('in', 'Inches'), ('ft', 'Feet'), ('cm', 'CM')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.CharField(blank=True, choices=[('3', '3'), ('1', '1'), ('4', '4'), ('5', '5'), ('2', '2')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='shippingsettings',
            name='shipping_status',
            field=models.CharField(blank=True, choices=[('unshipped', 'Unshipped'), ('shipped', 'Shipped'), ('preshipment', 'Pre-shipment'), ('delivered', 'Delivered')], max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ManyToManyField(blank=True, null=True, related_name='ds_mp_product_bookmark', to='ecommerce.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ds_mp_product_bookmark_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
