# Generated by Django 4.2 on 2023-04-17 11:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("webapp", "0039_rename_language_blogtranslation_lang"),
        ("ponds", "0020_rename_pondtexttransations_pondtexttransation"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="PondTextTransation",
            new_name="PondTextTranslation",
        ),
    ]
