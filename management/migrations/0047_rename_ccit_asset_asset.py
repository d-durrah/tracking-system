# Generated by Django 4.1.5 on 2023-02-05 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0046_rename_asset_ccit_asset'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CCIT_Asset',
            new_name='Asset',
        ),
    ]
