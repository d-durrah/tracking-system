# Generated by Django 4.1.5 on 2023-02-05 19:08

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0036_alter_device_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='device',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='supplier', chained_model_field='supplier', on_delete=django.db.models.deletion.CASCADE, to='management.device'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='supplier',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='category', chained_model_field='category', on_delete=django.db.models.deletion.CASCADE, to='management.supplier'),
        ),
    ]