# Generated by Django 4.0.5 on 2022-06-16 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_picture_description_en_alter_picture_slug_cs'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='enable',
            field=models.BooleanField(default=False, verbose_name='Zaponout'),
        ),
    ]