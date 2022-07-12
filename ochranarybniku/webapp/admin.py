from django.contrib import admin
from webapp.models import PhotoGallery, Picture, Page
from imagekit.admin import AdminThumbnail


class PictureInline(admin.TabularInline):
    model = Picture
    prepopulated_fields = {
        "slug_cs": ("description_cs",),
        "slug_en": ("description_en",),
    }
    thumbnail = AdminThumbnail(image_field="admin_thumbnail")
    thumbnail.short_description = "Náhled"
    readonly_fields = ("thumbnail",)


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = (
        "name_cs",
        "name_en",
        "description_cs",
        "description_en",
        "count_pictures",
        "enable",
    )
    list_filter = ("enable", "created", "modified")
    search_fields = ("name_cs", "description_cs", "name_en", "description_en")
    inlines = [
        PictureInline,
    ]
    prepopulated_fields = {
        "slug_cs": ("name_cs",),
        "slug_en": ("name_en",),
    }


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "description_cs",
        "description_en",
        "enable",
        "thumbnail",
    )
    search_fields = ("description_cs", "description_en", "enable")
    list_filter = ("enable", "photogallery")
    thumbnail = AdminThumbnail(image_field="admin_thumbnail")
    thumbnail.short_description = "Náhled"
    prepopulated_fields = {
        "slug_cs": ("description_cs",),
        "slug_en": ("description_en",),
    }


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('name_cs', 'name_en', "slug_cs", 'slug_en')
    prepopulated_fields = {
        "slug_cs": ("name_cs",),
        "slug_en": ("name_en",),
    }
