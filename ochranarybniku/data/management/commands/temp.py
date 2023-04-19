from django.core.management.base import BaseCommand, CommandError
import csv
import datetime
from dbfread import DBF
from django.utils.text import slugify

from webapp.models import PictureDescription, Picture, Language


class Command(BaseCommand):

    def handle(self, *args, **options):
        cs = Language.objects.get(lang='cs')
        en = Language.objects.get(lang='en')
        for a in DBF('/var/tmp/preklad_obrazky.dbf', encoding='utf-8'):
            print(a['ID'])
            p = Picture.objects.get(pk=a['ID'])
            d1 = PictureDescription()
            d1.picture = p
            d1.lang = cs
            d1.description = a['CS']
            d1.slug = slugify(a['CS'][:50])

            d2 = PictureDescription()
            d2.picture = p
            d2.lang = en
            d2.description = a['EN']
            d2.slug = slugify(a['EN'][:50])

            d1.save()
            d2.save()

