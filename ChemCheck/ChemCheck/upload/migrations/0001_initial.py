# Generated by Django 2.2 on 2019-06-01 17:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chemkin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_file', models.FileField(upload_to='uploads/')),
                ('timstamps', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
