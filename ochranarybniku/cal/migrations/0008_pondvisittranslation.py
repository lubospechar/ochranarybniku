# Generated by Django 4.2 on 2023-04-17 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("webapp", "0039_rename_language_blogtranslation_lang"),
        ("cal", "0007_pondvisit_desc_en"),
    ]

    operations = [
        migrations.CreateModel(
            name="PondVisitTranslation",
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
                ("desc", models.CharField(max_length=255)),
                (
                    "lang",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="webapp.language",
                    ),
                ),
                (
                    "visit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cal.pondvisit"
                    ),
                ),
            ],
        ),
    ]
