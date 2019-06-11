# Generated by Django 2.2.1 on 2019-06-11 16:25

from django.db import migrations, models
import upload.models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0006_auto_20190607_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemkin',
            name='mechanism_file',
            field=models.FileField(blank=True, null=True, upload_to=upload.models.upload_to),
        ),
        migrations.AlterField(
            model_name='chemkin',
            name='surface_file',
            field=models.FileField(blank=True, null=True, upload_to=upload.models.upload_to),
        ),
        migrations.AlterField(
            model_name='chemkin',
            name='thermo_file',
            field=models.FileField(blank=True, null=True, upload_to=upload.models.upload_to),
        ),
        migrations.AlterField(
            model_name='chemkin',
            name='transport_file',
            field=models.FileField(blank=True, null=True, upload_to=upload.models.upload_to),
        ),
    ]
