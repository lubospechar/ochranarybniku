# Generated by Django 4.0.6 on 2022-07-12 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_rename_pages_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='title',
            field=models.BooleanField(default=False),
        ),
    ]
