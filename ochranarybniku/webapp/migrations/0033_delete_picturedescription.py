# Generated by Django 4.2 on 2023-04-16 18:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("webapp", "0032_alter_picturedescription_description"),
    ]

    operations = [
        migrations.DeleteModel(
            name="PictureDescription",
        ),
    ]
