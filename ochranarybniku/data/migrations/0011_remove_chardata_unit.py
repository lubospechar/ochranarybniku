# Generated by Django 4.0.5 on 2022-06-23 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_alter_integerdata_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chardata',
            name='unit',
        ),
    ]
