# Generated by Django 5.0 on 2023-12-22 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodtruck',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='foodtruck',
            name='expiration_date',
        ),
    ]