# Generated by Django 4.1.5 on 2023-02-10 16:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management', '0052_rename_available_asset_available_to_borrow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_description', models.TextField()),
                ('purpose', models.TextField()),
                ('ID_number', models.CharField(max_length=8)),
                ('borrow_date', models.DateField(default=datetime.date.today)),
                ('return_date', models.DateField(default=datetime.date.today)),
                ('resource_asset_number', models.ForeignKey(limit_choices_to={'available_to_borrow': True}, on_delete=django.db.models.deletion.CASCADE, to='management.asset')),
            ],
        ),
        migrations.CreateModel(
            name='Current',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_description', models.TextField()),
                ('purpose', models.TextField()),
                ('ID_number', models.CharField(max_length=8)),
                ('borrow_date', models.DateField(default=datetime.date.today)),
                ('resource_asset_number', models.ForeignKey(limit_choices_to={'available_to_borrow': True}, on_delete=django.db.models.deletion.CASCADE, to='management.asset')),
            ],
        ),
    ]
