# Generated by Django 4.0.5 on 2022-06-16 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_photogallery_description_en_photogallery_name_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='description_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Popis fotografie (en)'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='slug_cs',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
