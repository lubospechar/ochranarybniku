from django.db import models
from django.contrib.gis.db.models import PolygonField
from webapp.models import Picture, PhotoGallery, Blog, PhotogaleryDescription, PictureDescription, Language
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from django.utils import translation

def get_lang():
    return Language.objects.get(
        lang = translation.get_language()
    )

class Pond(models.Model):
    pond_name = models.CharField(
        verbose_name='jméno rybníku', max_length=255,
    )
    
    area = PolygonField(
        verbose_name='Poloha rybníku (polyogon)'
    )
    
    area_m2 = models.PositiveIntegerField(verbose_name="Rozloha rybníku", null=True, blank=True)

    altitude = models.PositiveIntegerField(verbose_name="Nadmořská výška", null=True, blank=True)

    monitored = models.BooleanField(
        verbose_name="Sledovaný rybník",
        default=False
    )
    
    reserve = models.BooleanField(
        verbose_name="Rezerva",
        default=False
    )
    
    slug = models.SlugField()
    
    qr_code = models.ImageField(null=True, blank=True, upload_to="qrcodes/", verbose_name="QR Kód karty rybníku")
    
    title_picture = models.ImageField(null=True, blank=True, upload_to="pond_titles/", verbose_name="Titulní obrázek")

    title_picture_home = ImageSpecField(
        source="title_picture",
        processors=[ResizeToFit(800, 271, False)],
        format="JPEG",
        options={"quality": 70},
        id="home_page"
    )

    title_picture_list = ImageSpecField(
        source="title_picture",
        processors=[ResizeToFit(1172, 397, False)],
        format="JPEG",
        options={"quality": 70},
        id="list_page"
    )


    main_text_cs = models.TextField(verbose_name="Hlavní text (cs)", null=True, blank=True)
    main_photogallery = models.ManyToManyField(Picture, blank=True)
    
    
    photogalleries = models.ManyToManyField(PhotoGallery, blank=True)
    related_blogs = models.ManyToManyField(Blog, blank=True)
    
    def __str__(self):
        return self.pond_name

    def get_main_photogallery(self):
        pictures = self.main_photogallery.all()
        return PictureDescription.objects.filter(
            picture__in=pictures,
            lang=get_lang()
        )

    def get_related_photogalleries(self):
        galleries = self.photogalleries.all()
        return PhotogaleryDescription.objects.filter(
            photogallery__in = galleries,
            lang = Language.objects.get(
                lang = get_lang()
            )
        )


    def get_text(self):
        try:
            return self.pondtexttranslation_set.get(lang=get_lang()).text
        except PondTextTranslation.DoesNotExist:
            return None
    
    class Meta:
        verbose_name='Rybník'
        verbose_name_plural='Rybníky'


class PondTextTranslation(models.Model):
    lang = models.ForeignKey(Language, on_delete=models.Model)
    pond = models.ForeignKey(Pond, on_delete=models.Model)
    text = models.TextField()
