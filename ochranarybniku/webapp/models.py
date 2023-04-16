from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Language(models.Model):
    lang =  models.CharField(max_length=2)

    class Meta:
        verbose_name="Zapnutý jazyk"
        verbose_name_plural="Zapnuté jazyky"

    def __str__(self):
        return self.lang

class Page(models.Model):
    name = models.CharField(max_length=255, verbose_name="Název")
    content = models.TextField(verbose_name="Obash (html)")
    slug = models.SlugField()
    enable = models.BooleanField(verbose_name="Zapnuto")
    lang = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Jazyk")
    add_to_title = models.BooleanField(verbose_name="Přidat na titulní stránku", default=False)

    class Meta:
        verbose_name="Stránka"
        verbose_name_plural="Stránky"

class PhotoGallery(models.Model):
    name_cs = models.CharField(max_length=255, verbose_name="Název galerie (cs)")
    description_cs = models.TextField(
        verbose_name="Popis fotogalerie (cs)", null=True, blank=True
    )
    modified = models.DateTimeField(auto_now=True, verbose_name="poslední úprava")
    created = models.DateTimeField(auto_now_add=True, verbose_name="vytvořeno")
    slug_cs = models.SlugField()

    enable = models.BooleanField(default=False, verbose_name="Zaponout")

    class Meta:
        verbose_name = "Fotogalerie"
        verbose_name_plural = "Fotogalerie"

    def __str__(self):
        return self.name_cs

    def count_pictures(self):
        # spočítá kolik obrázků fotogalerie obsahuje
        return self.pictures.all().count()
    
    def get_title(self):
        try:
            return self.pictures.get(title=True)
        except Picture.MultipleObjectsReturned:
            return self.pictures.filter(title=True)[0]
        except Picture.DoesNotExist:
            return self.pictures.all()[0]
        

    count_pictures.short_description = "Počet obrázků"


class Picture(models.Model):
    photogallery = models.ForeignKey(
        PhotoGallery,
        on_delete=models.CASCADE,
        verbose_name="fotogalerie",
        related_name="pictures",
    )
    description_cs = models.CharField(
        max_length=255, verbose_name="Popis fotografie (cs)"
    )

    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/", verbose_name="Obrázek (soubor)"
    )
    admin_thumbnail = ImageSpecField(
        source="photo",
        processors=[ResizeToFit(300, 300)],
        format="JPEG",
        options={"quality": 60},
        id="image_thumbnail",
    )

    gallery_resize = ImageSpecField(
        source="photo",
        processors=[ResizeToFit(1600, 1600)],
        format="JPEG",
        options={"quality": 75},
        id="image_gallery_resize",
    )

    slug_cs = models.SlugField()

    enable = models.BooleanField(default=False, verbose_name="Zaponout")

    title = models.BooleanField(default=False)
    class Meta:
        verbose_name = "Obrázek"
        verbose_name_plural = "Obrázky"

    def __str__(self):
        return f"{self.photogallery.name_cs} / {self.description_cs}"


class Blog(models.Model):
    headline_cs = models.CharField(
        max_length=255, verbose_name="Nadpis"
    )
    
    slug_cs = models.SlugField()
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modified = models.DateTimeField(auto_now=True, verbose_name="Poslední úprava")
    published = models.DateTimeField(auto_now_add=True, verbose_name="Publikováno")
    
    text=models.TextField(verbose_name="obsah")
    
    photogalleries = models.ManyToManyField(PhotoGallery, verbose_name="fotogralerie", blank=True)
    pictures = models.ManyToManyField(Picture, verbose_name="obrázky", blank=True)
    
    
    enable = models.BooleanField(verbose_name="Zapnout", default=False)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogy"

    def get_pictures(self):
        pictures = list()
        for picture in self.pictures.all():
            pictures.append(picture)
        
        for photogallery in self.photogalleries.all():
            for picture in photogallery.pictures.all():
                pictures.append(picture)
        
        return pictures
            
