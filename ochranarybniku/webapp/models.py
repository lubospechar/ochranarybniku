from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils import translation
from django.utils.safestring import mark_safe

class Language(models.Model):
    lang =  models.CharField(max_length=2)

    class Meta:
        verbose_name="Zapnutý jazyk"
        verbose_name_plural="Zapnuté jazyky"

    def __str__(self):
        return self.lang

    @staticmethod
    def cs():
        return Language.objects.get(lang='cs')

def get_lang():
    return Language.objects.get(
        lang = translation.get_language()
    )

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
    modified = models.DateTimeField(auto_now=True, verbose_name="poslední úprava")
    created = models.DateTimeField(auto_now_add=True, verbose_name="vytvořeno")
    slug = models.SlugField()

    enable = models.BooleanField(default=False, verbose_name="Zaponout")

    class Meta:
        verbose_name = "Fotogalerie"
        verbose_name_plural = "Fotogalerie"

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
        
    def __str__(self):
        try:
            return PhotogaleryDescription.objects.get(photogallery=self, lang=Language.cs()).name
        except PhotogaleryDescription.DoesNotExist:
            return 'Nepojmenováno'




    count_pictures.short_description = "Počet obrázků"

class PhotogaleryDescription(models.Model):
    photogallery = models.ForeignKey(PhotoGallery, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Název galerie")
    description = models.TextField(
        verbose_name="Popis fotogalerie", null=True, blank=True
    )
    lang = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Jazyk")
    slug = models.SlugField()

class Picture(models.Model):
    photogallery = models.ForeignKey(
        PhotoGallery,
        on_delete=models.CASCADE,
        verbose_name="fotogalerie",
        related_name="pictures",
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

    enable = models.BooleanField(default=False, verbose_name="Zaponout")

    title = models.BooleanField(default=False)

    def __str__(self):
        try:
            return PictureDescription.objects.get(picture=self, lang=Language.cs()).description
        except PictureDescription.DoesNotExist:
            return 'Nepojmenováno'

    class Meta:
        verbose_name = "Obrázek"
        verbose_name_plural = "Obrázky"


class PictureDescription(models.Model):
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    description = models.CharField(
        max_length=255,
        verbose_name="Popis obrázku"
    )
    lang = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Jazyk")
    slug = models.SlugField()

class Blog(models.Model):
    headline_cs = models.CharField(
        max_length=255, verbose_name="Nadpis"
    )
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modified = models.DateTimeField(auto_now=True, verbose_name="Poslední úprava")
    published = models.DateTimeField(auto_now_add=True, verbose_name="Publikováno")
    
    text=models.TextField(verbose_name="obsah")
    
    photogalleries = models.ManyToManyField(PhotoGallery, verbose_name="fotogralerie", blank=True)
    pictures = models.ManyToManyField(Picture, verbose_name="obrázky", blank=True)
    youtube = models.CharField(verbose_name="YouTube ID", null=True, blank=True, max_length=30)
    
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

    def get_slug(self):
        return BlogTranslation.objects.get(
            blog=self,
            lang=get_lang()
        ).slug

    def get_headline(self):
        return BlogTranslation.objects.get(
            blog=self,
            lang=get_lang()
        ).headline

    def get_text(self):
        return BlogTranslation.objects.get(
            blog=self,
            lang=get_lang()
        ).text

    def get_pictures(self):
        return PictureDescription.objects.filter(
            lang=get_lang(),
            picture__in=Picture.objects.filter(
                photogallery__in=self.photogalleries.all()
            )
        )
            
class BlogTranslation(models.Model):
    headline = models.CharField(max_length=255)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    slug = models.SlugField()

    def get_pictures(self):
        pictures = PictureDescription.objects.filter(
            lang=self.lang,
            picture__in=Picture.objects.filter(
                photogallery__in=self.blog.photogalleries.all()
            )
        )

        return pictures

class Storage(models.Model):
    name = models.CharField(max_length=255)
    data = models.FileField(upload_to='data/%Y/%m/%d/')

    def hypertext(self):
        return f'<li><a href="{ self.data.url }">{ self.name }</a></li>'
