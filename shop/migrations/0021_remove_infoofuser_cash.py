# Generated by Django 3.1 on 2020-08-17 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_infoofuser_cash'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infoofuser',
            name='cash',
        ),
    ]