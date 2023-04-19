# Generated by Django 4.2 on 2023-04-17 11:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("webapp", "0039_rename_language_blogtranslation_lang"),
        ("ponds", "0018_pond_related_blogs"),
    ]

    operations = [
        migrations.CreateModel(
            name="PondTextTransations",
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
                ("text", models.TextField()),
                (
                    "language",
                    models.ForeignKey(on_delete=models.Model, to="webapp.language"),
                ),
                ("pond", models.ForeignKey(on_delete=models.Model, to="ponds.pond")),
            ],
        ),
    ]
