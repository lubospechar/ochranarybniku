# Generated by Django 4.2 on 2023-04-17 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("webapp", "0039_rename_language_blogtranslation_lang"),
        ("data", "0026_remove_fiedlerdata_unit_remove_floatdata_unit_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ParameterTranslation",
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
                ("name", models.CharField(max_length=255)),
                ("note", models.CharField(max_length=255)),
                (
                    "lang",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="webapp.language",
                    ),
                ),
                (
                    "parameter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="data.parameter"
                    ),
                ),
            ],
        ),
    ]
