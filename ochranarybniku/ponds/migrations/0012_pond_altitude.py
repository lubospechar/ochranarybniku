# Generated by Django 4.1 on 2022-08-08 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ponds", "0011_alter_pond_main_photogallery_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="pond",
            name="altitude",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Nadmořská výška"
            ),
        ),
    ]
