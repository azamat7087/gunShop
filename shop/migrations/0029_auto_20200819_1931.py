# Generated by Django 3.1 on 2020-08-19 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0028_auto_20200819_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoofuser',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/images/users/'),
        ),
    ]