# Generated by Django 4.0.6 on 2022-07-31 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ponds', '0008_pond_qr_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pond',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qrcodes/', verbose_name='QR Kód karty rybníku'),
        ),
    ]