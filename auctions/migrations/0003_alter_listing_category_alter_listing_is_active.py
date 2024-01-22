# Generated by Django 5.0 on 2024-01-22 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_category_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='auctions.category'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]