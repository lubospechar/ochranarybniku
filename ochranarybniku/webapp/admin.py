from django.contrib import admin
from webapp.models import PhotoGallery, Picture
from imagekit.admin import AdminThumbnail
from django.contrib.contenttypes.admin import GenericTabularInline


class PictureInline(admin.TabularInline):
    model = Picture
    prepopulated_fields = {
        "slug": ("description",),
    }
    thumbnail = AdminThumbnail(image_field="admin_thumbnail")
    thumbnail.short_description = "Náhled"
    readonly_fields = ("thumbnail",)


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    inlines = [
        PictureInline,
    ]
    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ("__str__", "thumbnail")
    thumbnail = AdminThumbnail(image_field="admin_thumbnail")
    prepopulated_fields = {
        "slug": ("description",),
    }
