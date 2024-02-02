# Generated by Django 5.0 on 2024-02-02 10:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_listing_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='watch_list',
            field=models.ManyToManyField(blank=True, null=True, related_name='listing_watch_list', to=settings.AUTH_USER_MODEL),
        ),
    ]
