# Generated by Django 4.0.5 on 2022-06-23 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_rename_description_unit_description_cs'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='description_en',
            field=models.CharField(default=1, max_length=255, verbose_name='Popis (en)'),
            preserve_default=False,
        ),
    ]
