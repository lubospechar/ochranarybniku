# Generated by Django 4.0.5 on 2022-06-23 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_booleandata_parameter_chardata_parameter_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booleandata',
            name='unit',
        ),
    ]
