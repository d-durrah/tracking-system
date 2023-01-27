# Generated by Django 4.1.5 on 2023-01-25 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_remove_device_bill_number_remove_device_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='bill_number',
            field=models.CharField(default='000', max_length=255),
        ),
        migrations.AddField(
            model_name='device',
            name='resource_asset_number',
            field=models.BigIntegerField(default='000'),
        ),
        migrations.AddField(
            model_name='device',
            name='supplier',
            field=models.CharField(default='Enter supplier name...', max_length=255),
        ),
        migrations.AlterField(
            model_name='device',
            name='description',
            field=models.TextField(default='Add a description...'),
        ),
    ]
