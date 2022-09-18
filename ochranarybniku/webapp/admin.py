from django.contrib import admin
from webapp.models import PhotoGallery, Picture, Page, Blog
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


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("headline_cs", "author", 'modified', 'published', 'enable')
    list_filter = ("enable", "published", "modified")
    search_fields = ("headline_cs",)
    filter_horizontal = ('photogalleries', 'pictures',)
    prepopulated_fields = {
        "slug_cs": ("headline_cs",),
    }
