# Generated by Django 3.1 on 2020-08-27 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0035_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='gun',
            new_name='gun_main',
        ),
    ]
