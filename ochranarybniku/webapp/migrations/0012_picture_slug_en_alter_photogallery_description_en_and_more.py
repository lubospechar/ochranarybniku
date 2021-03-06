# Generated by Django 4.0.5 on 2022-06-16 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_photogallery_enable'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='slug_en',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='photogallery',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Popis fotogalerie (en)'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='slug_cs',
            field=models.SlugField(),
        ),
    ]
