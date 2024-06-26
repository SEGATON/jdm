# Generated by Django 4.2.2 on 2024-03-31 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ds_mp_app', '0007_order_refund_requested_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refunds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_for_refund', models.TextField(blank=True, max_length=300, null=True)),
                ('refund_accepted', models.BooleanField(default=False)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ds_mp_app.order')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='refund_for_user_ds_mp', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
