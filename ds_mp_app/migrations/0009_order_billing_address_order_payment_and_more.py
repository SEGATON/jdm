# Generated by Django 4.2.2 on 2024-03-31 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0015_alter_productsize_size_alter_productsize_size_label_and_more'),
        ('ds_mp_app', '0008_refunds'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='billing_address_ds_mp', to='ecommerce.address'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment_ds_mp', to='ecommerce.payment'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipping_address_ds_mp', to='ecommerce.address'),
        ),
    ]
