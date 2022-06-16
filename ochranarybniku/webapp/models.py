from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


class PhotoGallery(models.Model):
    name_cs = models.CharField(max_length=255, verbose_name="Název galerie (cs)")
    description_cs = models.TextField(
        verbose_name="Popis fotogalerie (cs)", null=True, blank=True
    )
    name_en = models.CharField(max_length=255, verbose_name="Název galerie (en)", null=True, blank=True)
    description_en = models.TextField(
        verbose_name="Popis fotogalerie (cs)", null=True, blank=True
    )
    modified = models.DateTimeField(auto_now=True, verbose_name="poslední úprava")
    created = models.DateTimeField(auto_now_add=True, verbose_name="vytvořeno")
    slug_cs = models.SlugField()
    slug_en = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name = "Fotogalerie"
        verbose_name_plural = "Fotogalerie"

    def __str__(self):
        return self.name_cs

    def count_pictures(self):
        # spočítá kolik obrázků fotogalerie obsahuje
        return self.pictures.all().count()

    count_pictures.short_description = "Počet obrázků"


class Picture(models.Model):
    photogallery = models.ForeignKey(
        PhotoGallery,
        on_delete=models.CASCADE,
        verbose_name="fotogalerie",
        related_name="pictures",
    )
    description_cs = models.CharField(max_length=255, verbose_name="Popis fotografie (cs)")
    description_en = models.CharField(max_length=255, verbose_name="Popis fotografie (en)", null=True, blank=True)
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/", verbose_name="Obrázek (soubor)"
    )
    admin_thumbnail = ImageSpecField(
        source="photo",
        processors=[ResizeToFit(300, 300)],
        format="JPEG",
        options={"quality": 60},
    )
    slug_cs = models.SlugField()
    slug_cs = models.SlugField(null=True, blank=True)

    enable = models.BooleanField(default=False, verbose_name="Zaponout")

    class Meta:
        verbose_name = "Obrázek"
        verbose_name_plural = "Obrázky"

    def __str__(self):
        return f"{self.photogallery.name_cs} / {self.description_cs}"
