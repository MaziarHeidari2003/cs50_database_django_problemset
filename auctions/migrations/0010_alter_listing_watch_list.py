# Generated by Django 5.0 on 2024-02-03 12:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_bid_alter_listing_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='watch_list',
            field=models.ManyToManyField(blank=True, related_name='listing_watch_list', to=settings.AUTH_USER_MODEL),
        ),
    ]
