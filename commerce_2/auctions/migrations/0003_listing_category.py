# Generated by Django 5.0 on 2024-02-06 12:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listing_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listing_category', to='auctions.category'),
        ),
    ]