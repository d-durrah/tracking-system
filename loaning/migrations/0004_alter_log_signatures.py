# Generated by Django 4.1.5 on 2023-02-15 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loaning', '0003_alter_log_signatures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='signatures',
            field=models.ImageField(null=True, upload_to='uploads/signature_archive'),
        ),
    ]