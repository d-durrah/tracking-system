# Generated by Django 4.1.5 on 2023-02-05 19:41

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0037_alter_asset_device_alter_asset_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='device',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='supplier__category', chained_model_field='supplier__category', on_delete=django.db.models.deletion.CASCADE, to='management.device'),
        ),
    ]
