# Generated by Django 4.1.2 on 2022-10-05 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0022_alter_pondmeasurement_datetime"),
    ]

    operations = [
        migrations.CreateModel(
            name="FiedlerData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "note",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Poznámka"
                    ),
                ),
                ("value", models.FloatField(verbose_name="Hodnota")),
                (
                    "measurement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data.pondmeasurement",
                        verbose_name="Měření",
                    ),
                ),
                (
                    "parameter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data.parameter",
                        verbose_name="Parametr",
                    ),
                ),
                (
                    "unit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data.unit",
                        verbose_name="Jednotky",
                    ),
                ),
            ],
            options={
                "verbose_name": "Data ze stanic (desetinné číslo)",
                "verbose_name_plural": "Data ze stanic (desetinná čísla)",
            },
        ),
    ]
