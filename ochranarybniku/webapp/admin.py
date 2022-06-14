from django.contrib import admin
from webapp.models import PhotoGallery, Picture

@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    pass

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    pass
