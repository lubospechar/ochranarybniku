# Generated by Django 4.0.5 on 2022-06-14 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_photo_photogallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Obrázek', 'verbose_name_plural': 'Obrázky'},
        ),
    ]
