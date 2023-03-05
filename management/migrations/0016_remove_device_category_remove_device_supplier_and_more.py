# Generated by Django 4.1.5 on 2023-03-05 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0015_alter_asset_options_remove_asset_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='category',
        ),
        migrations.RemoveField(
            model_name='device',
            name='supplier',
        ),
        migrations.AlterUniqueTogether(
            name='supplier',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Device',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
    ]