# Generated by Django 3.0 on 2019-12-07 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0016_auto_20191207_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sq',
            name='Age',
            field=models.CharField(blank=True, choices=[('adult', 'Adult'), ('juvenile', 'Juvenile'), ('', '')], default='', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sq',
            name='Location',
            field=models.CharField(blank=True, choices=[('adult', 'Ground Plane'), ('juvenile', 'Above Ground'), ('', '')], default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sq',
            name='Primary_Fur_Color',
            field=models.CharField(blank=True, choices=[('gray', 'Gray'), ('black', 'Black'), ('cinnamon', 'Cinnamon'), ('', '')], default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sq',
            name='Shift',
            field=models.CharField(blank=True, choices=[('am', 'AM'), ('pm', 'PM'), ('', '')], default='', max_length=20, null=True),
        ),
    ]
