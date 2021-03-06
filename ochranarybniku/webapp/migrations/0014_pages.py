# Generated by Django 4.0.6 on 2022-07-12 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_merge_20220616_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cs', models.CharField(max_length=255, verbose_name='Název (cs)')),
                ('name_en', models.CharField(max_length=255, verbose_name='Název (en)')),
                ('content_cs', models.TextField()),
                ('content_en', models.TextField()),
                ('slug_cs', models.SlugField()),
                ('slug_en', models.SlugField()),
                ('enable', models.BooleanField()),
            ],
        ),
    ]
