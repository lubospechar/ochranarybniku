from django.db import models
from django.contrib.gis.db.models import PolygonField
from webapp.models import Picture, PhotoGallery

class Pond(models.Model):
    pond_name = models.CharField(
        verbose_name='jméno rybníku', max_length=255,
    )
    
    area = PolygonField(
        verbose_name='Poloha rybníku (polyogon)'
    )
    
    area_m2 = models.PositiveIntegerField(verbose_name="Rozloha rybníku", null=True, blank=True)

    monitored = models.BooleanField(
        verbose_name="Sledovaný rybník",
        default=False
    )
    
    slug = models.SlugField()
    
    qr_code = models.ImageField(null=True, blank=True, upload_to="qrcodes/", verbose_name="QR Kód karty rybníku")
    
    main_text = models.TextField(verbose_name="Hlavní text", null=True, blank=True)
    main_photogallery = models.ManyToManyField(Picture, blank=True)
    
    photogalleries = models.ManyToManyField(PhotoGallery, blank=True)
    
    def __str__(self):
        return self.pond_name
    
    class Meta:
        verbose_name='Rybník'
        verbose_name_plural='Rybníky'
