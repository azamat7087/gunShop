# Generated by Django 3.1 on 2020-08-16 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/images/guns/'),
        ),
    ]
