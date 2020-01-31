# Generated by Django 3.0 on 2019-12-08 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0017_auto_20191207_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sq',
            name='Age',
            field=models.CharField(blank=True, choices=[('adult', 'Adult'), ('juvenile', 'Juvenile'), ('', '')], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='sq',
            name='Date',
            field=models.DateField(blank=True, default=None, help_text='YYYY-MM-DD'),
        ),
        migrations.AlterField(
            model_name='sq',
            name='Latitude',
            field=models.FloatField(blank=True, default=None, help_text='latitude coordinate'),
        ),
        migrations.AlterField(
            model_name='sq',
            name='Location',
            field=models.CharField(blank=True, choices=[('adult', 'Ground Plane'), ('juvenile', 'Above Ground'), ('', '')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='sq',
            name='Longitude',
            field=models.FloatField(blank=True, default=None, help_text='longitude coordinate'),
        ),
        migrations.AlterField(
            model_name='sq',
            name='Other_Activities',
            field=models.CharField(blank=True, default=None, help_text='describe squirrels other activities', max_length=100),
        ),
        migrations.AlterField(
            model_name='sq',
            name='Primary_Fur_Color',
            field=models.CharField(blank=True, choices=[('gray', 'Gray'), ('black', 'Black'), ('cinnamon', 'Cinnamon'), ('', '')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='sq',
            name='Shift',
            field=models.CharField(blank=True, choices=[('am', 'AM'), ('pm', 'PM'), ('', '')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='sq',
            name='Specific_Location',
            field=models.CharField(blank=True, default=None, help_text='commentary on the squirrel location', max_length=100),
        ),
    ]