# Generated by Django 4.1.5 on 2023-02-05 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0049_alter_category_options_alter_device_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='device',
            options={},
        ),
    ]