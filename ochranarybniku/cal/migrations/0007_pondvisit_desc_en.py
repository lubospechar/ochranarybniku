# Generated by Django 4.1 on 2022-08-09 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cal", "0006_alter_pondvisit_ponds"),
    ]

    operations = [
        migrations.AddField(
            model_name="pondvisit",
            name="desc_en",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Stručný popis práce (en)",
            ),
        ),
    ]