# Generated by Django 5.0 on 2024-01-22 12:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_listing_category_alter_listing_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='watch_list',
            field=models.ManyToManyField(blank=True, related_name='listingwatchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
