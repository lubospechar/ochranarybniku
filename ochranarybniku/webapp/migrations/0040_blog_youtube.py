# Generated by Django 4.1.3 on 2023-04-19 12:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("webapp", "0039_rename_language_blogtranslation_lang"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="youtube",
            field=models.URLField(
                blank=True, null=True, verbose_name="Odkaz na youtube"
            ),
        ),
    ]
