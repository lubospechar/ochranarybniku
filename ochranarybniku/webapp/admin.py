from django.contrib import admin
from webapp.models import PhotoGallery, Picture, Page
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
    list_display = (
        "name_cs",
        "description_cs",
        "count_pictures",
        "enable",
    )
    list_filter = ("enable", "created", "modified")
    search_fields = ("name_cs", "description_cs")
    inlines = [
        PictureInline,
    ]
    prepopulated_fields = {
        "slug_cs": ("name_cs",),
    }


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "description_cs",
        "enable",
        "thumbnail",
    )
    search_fields = ("description_cs", "enable")
    list_filter = ("enable", "photogallery")
    thumbnail = AdminThumbnail(image_field="admin_thumbnail")
    thumbnail.short_description = "Náhled"
    prepopulated_fields = {
        "slug_cs": ("description_cs",),
    }


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('name_cs', "slug_cs")
    prepopulated_fields = {
        "slug_cs": ("name_cs",),
    }
