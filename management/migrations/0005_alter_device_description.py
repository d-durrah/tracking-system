# Generated by Django 4.1.5 on 2023-01-25 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_device_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='description',
            field=models.TextField(default='Add a description (max words: 900)...', max_length=900),
        ),
    ]
