# Generated by Django 4.1.5 on 2023-02-15 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loaning', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='signatures',
            field=models.ImageField(default='1', upload_to='uploads/signature_archive'),
        ),
    ]
