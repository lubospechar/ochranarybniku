# Generated by Django 4.2 on 2023-04-16 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("webapp", "0027_rename_description_cs_photogallery_description_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PhotogaleryDescription",
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
                    "name",
                    models.CharField(max_length=255, verbose_name="Název galerie (cs)"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Popis fotogalerie (cs)"
                    ),
                ),
                (
                    "lang",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="webapp.language",
                        verbose_name="Jazyk",
                    ),
                ),
                (
                    "photogallery",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="webapp.photogallery",
                    ),
                ),
            ],
        ),
    ]