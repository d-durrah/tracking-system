# Generated by Django 4.1.5 on 2023-01-26 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0018_alter_device_resource_asset_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='bill_number',
            field=models.CharField(max_length=255),
        ),
    ]
