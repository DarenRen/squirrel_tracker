# Generated by Django 2.2.7 on 2019-12-07 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0011_auto_20191207_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sq',
            name='Date',
            field=models.DateField(help_text='month, day, and year (MMDDYYYY)'),
        ),
    ]
