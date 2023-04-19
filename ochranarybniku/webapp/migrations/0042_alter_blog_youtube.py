# Generated by Django 4.1.3 on 2023-04-19 12:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("webapp", "0041_alter_blog_youtube"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="youtube",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="YouTube ID"
            ),
        ),
    ]
