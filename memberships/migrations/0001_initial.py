# Generated by Django 4.2.2 on 2024-03-08 10:14

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecommerce', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biography', ckeditor.fields.RichTextField(blank=True, max_length=10000, null=True)),
                ('profile_photo', easy_thumbnails.fields.ThumbnailerImageField(default='/MEMBERSHIP/PROFILE_PHOTOS/default_profile_photo.png', upload_to='PROFILE_PHOTOS')),
                ('website_url', models.URLField(blank=True, max_length=1000, null=True)),
                ('twitter', models.URLField(blank=True, max_length=1000, null=True)),
                ('facebook', models.URLField(blank=True, max_length=1000, null=True)),
                ('youtube', models.URLField(blank=True, max_length=1000, null=True)),
                ('instagram', models.URLField(blank=True, max_length=1000, null=True)),
                ('bookmarks', models.ManyToManyField(blank=True, null=True, related_name='bookmarks', to='ecommerce.product')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
                ('wishlists', models.ManyToManyField(blank=True, null=True, related_name='wishlists', to='ecommerce.wishlist')),
            ],
        ),
    ]
