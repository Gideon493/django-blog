# Generated by Django 4.0.6 on 2022-08-23 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='dob',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
