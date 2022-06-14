from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


class PhotoGallery(models.Model):
    name = models.CharField(max_length=255, verbose_name="Název galerie")
    description = models.TextField(
        verbose_name="Popis fotogalerie", null=True, blank=True
    )
    modified = models.DateTimeField(auto_now=True, verbose_name="poslední úprava")
    created = models.DateTimeField(auto_now_add=True, verbose_name="vytvořeno")
    slug = models.SlugField()

    class Meta:
        verbose_name = "Fotogalerie"
        verbose_name_plural = "Fotogalerie"

    def __str__(self):
        return self.name

    def count_pictures(self):
        # spočítá kolik obrázků fotogalerie obsahuje
        return self.pictures.all().count()
    count_pictures.short_description = "Počet obrázků"

class Picture(models.Model):
    photogallery = models.ForeignKey(
        PhotoGallery, on_delete=models.CASCADE, verbose_name="fotogalerie", related_name="pictures"
    )
    description = models.CharField(max_length=255, verbose_name="Popis fotografie")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Obrázek (soubor)")
    admin_thumbnail = ImageSpecField(
        source="photo",
        processors=[ResizeToFit(300, 300)],
        format="JPEG",
        options={"quality": 60},
    )
    slug = models.SlugField()

    class Meta:
        verbose_name = "Obrázek"
        verbose_name_plural = "Obrázky"

    def __str__(self):
        return f'{self.photogallery.name} / {self.description}'
