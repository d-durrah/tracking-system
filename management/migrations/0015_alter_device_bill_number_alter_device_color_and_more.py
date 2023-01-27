# Generated by Django 4.1.5 on 2023-01-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0014_device_color_device_memory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='bill_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='device',
            name='color',
            field=models.CharField(choices=[('WHITE', 'White'), ('GRAY', 'Gray'), ('BLACK', 'Black'), ('RED', 'Red'), ('PINK', 'Pink'), ('BLUE', 'Blue'), ('GREEN', 'Green'), ('YELLOW', 'Yellow'), ('ORANGE', 'Orange'), ('PURPLE', 'Purple')], default='BLACK', max_length=10),
        ),
        migrations.AlterField(
            model_name='device',
            name='description',
            field=models.TextField(help_text='Add a description...', null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='resource_asset_number',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='device',
            name='supplier',
            field=models.CharField(help_text='Enter supplier name...', max_length=255),
        ),
    ]
