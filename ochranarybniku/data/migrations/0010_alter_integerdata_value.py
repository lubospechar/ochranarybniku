# Generated by Django 4.0.5 on 2022-06-23 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_rename_boolean_data_booleandata_value_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integerdata',
            name='value',
            field=models.IntegerField(verbose_name='Hodnota'),
        ),
    ]
