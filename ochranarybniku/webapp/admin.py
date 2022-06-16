from django.contrib import admin
from webapp.models import PhotoGallery, Picture
from imagekit.admin import AdminThumbnail


class PictureInline(admin.TabularInline):
    model = Picture
    prepopulated_fields = {
        "slug_cs": ("description_cs",),
    }
    thumbnail = AdminThumbnail(image_field="admin_thumbnail")
    thumbnail.short_description = "Náhled"
    readonly_fields = ("thumbnail",)


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ("name_cs", "description_cs", "count_pictures")
    list_filter = ("created", "modified")
    search_fields = ("name_cs", "description_cs")
    inlines = [
        PictureInline,
    ]
    prepopulated_fields = {
        "slug_cs": ("name_cs",),
        "slug_en": ("name_en",),
    }


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ("__str__", "thumbnail")
    thumbnail = AdminThumbnail(image_field="admin_thumbnail")
    thumbnail.short_description = "Náhled"
    prepopulated_fields = {
        "slug_cs": ("description_cs",),
        "slug_en": ("description_en",),
    }
