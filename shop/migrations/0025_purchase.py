# Generated by Django 3.1 on 2020-08-18 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_guns_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(db_index=True, max_length=150)),
                ('gun_slug', models.CharField(blank=True, max_length=30)),
                ('date_of_add', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to='static/images/guns/')),
            ],
            options={
                'ordering': ['-date_of_add'],
            },
        ),
    ]