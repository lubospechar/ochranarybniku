# vyžaduje balíky django-imagekit a pillow
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class PhotoGallery(models.Model):
    name = models.CharField(max_length=255, verbose_name="Název galerie")
    description = models.TextField(
        verbose_name="Popis fotogalerie", null=True, blank=True
    )
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    class Meta:
        verbose_name = "Fotogalerie"
        verbose_name_plural = "Fotogalerie"


class Picture(models.Model):
    photogallery = models.ForeignKey(
        PhotoGallery, on_delete=models.CASCADE, verbose_name="fotogalerie"
    )
    description = models.CharField(max_length=255, verbose_name="Popis fotografie")
    photo = models.ImageField(upload_to="photos")
    admin_thumbnail = ImageSpecField(
        source="photos/thumbnails",
        processors=[ResizeToFill(100, 50)],
        format="JPEG",
        options={"quality": 60},
    )
    slug = models.SlugField()

    class Meta:
        verbose_name = "Obrázek"
        verbose_name_plural = "Obrázky"
