# Generated by Django 3.1.2 on 2020-10-26 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20201026_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='alumni_status',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='pages.alumni_status'),
        ),
    ]
