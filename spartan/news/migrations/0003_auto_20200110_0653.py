# Generated by Django 3.0 on 2020-01-10 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200109_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
