# Generated by Django 4.1.5 on 2023-02-28 13:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_rename_asset_name_asset_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='production_date',
        ),
        migrations.AlterField(
            model_name='asset',
            name='purchase_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
