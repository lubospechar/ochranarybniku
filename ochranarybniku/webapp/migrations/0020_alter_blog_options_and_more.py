# Generated by Django 4.1.1 on 2022-09-23 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0019_blog_slug_cs"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={"verbose_name": "Blog", "verbose_name_plural": "Blogy"},
        ),
        migrations.RemoveField(
            model_name="photogallery",
            name="description_en",
        ),
    ]
