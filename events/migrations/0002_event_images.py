# Generated by Django 3.0.5 on 2020-07-13 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='images',
            field=models.ImageField(blank=True, upload_to='events'),
        ),
    ]
