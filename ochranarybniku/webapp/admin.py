from django.contrib import admin
from webapp.models import PhotoGallery, Picture

@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('description',), }
