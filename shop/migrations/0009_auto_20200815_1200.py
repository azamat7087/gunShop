# Generated by Django 3.1 on 2020-08-15 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20200815_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Knifes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='guns',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
