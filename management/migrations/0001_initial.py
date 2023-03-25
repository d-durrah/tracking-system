# Generated by Django 4.1.5 on 2023-03-25 11:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_id', models.CharField(max_length=100, unique=True)),
                ('resource_asset_number', models.CharField(max_length=255, null=True, unique=True)),
                ('model', models.CharField(max_length=255)),
                ('manufacturer', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('user_email', models.CharField(max_length=255)),
                ('purchase_date', models.DateTimeField(default=datetime.datetime.today, null=True)),
                ('bill_number', models.CharField(max_length=255, null=True)),
                ('bill_image', models.ImageField(null=True, upload_to='uploads/bill_archive')),
                ('available_to_borrow', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'CCIT Asset',
                'verbose_name_plural': 'CCIT Assets',
            },
        ),
    ]
