# Generated by Django 4.0.6 on 2022-08-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0003_members_idnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='photo',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
