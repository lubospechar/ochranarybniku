from django.contrib import admin
from webapp.models import (
    PhotoGallery, Picture, Page, Blog,
    Language, PhotogaleryDescription, PictureDescription,
    BlogTranslation
)
from imagekit.admin import AdminThumbnail

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("lang", )

class PictureInline(admin.TabularInline):
    model = Picture
    thumbnail = AdminThumbnail(image_field="admin_thumbnail")
    thumbnail.short_description = "Náhled"
    readonly_fields = ("thumbnail",)

class PhotogaleryDescriptionInline(admin.TabularInline):
    model = PhotogaleryDescription
    prepopulated_fields = {
        "slug": ("name",),
    }
    extra = 2

@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = (
        "count_pictures",
        "enable",
    )
    list_filter = ("enable", "created", "modified")
    # search_fields = ("name", "description")
    inlines = [
        PhotogaleryDescriptionInline,
        PictureInline,
    ]

@admin.register(PhotogaleryDescription)
class PhotogaleryDescriptionAdmin(admin.ModelAdmin):
    pass

class PictureDescriptionInline(admin.TabularInline):
    model = PictureDescription
    prepopulated_fields = {
        "slug": ("description",),
    }
    extra = 2

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "enable",
        "thumbnail",
    )
    search_fields = ("description_cs", "enable")
    list_filter = ("enable", "photogallery")
    thumbnail = AdminThumbnail(image_field="admin_thumbnail")
    thumbnail.short_description = "Náhled"

    inlines = [
        PictureDescriptionInline,
    ]


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('name', "slug", 'lang', 'enable', 'add_to_title',)
    list_filter = ('lang', 'add_to_title',)
    prepopulated_fields = {
        "slug": ("name",),
    }

class BlogTranslationInline(admin.TabularInline):
    model = BlogTranslation
    extra = 2
    prepopulated_fields = {
        "slug": ("headline",),
    }

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("headline_cs", "author", 'modified', 'published', 'enable')
    list_filter = ("enable", "published", "modified")
    search_fields = ("headline_cs",)
    filter_horizontal = ('photogalleries', 'pictures',)

    inlines = [
        BlogTranslationInline,
    ]



# @admin.register(PictureDescription)
# class PictureDescriptionAdmin(admin.ModelAdmin):
#     list_filter
