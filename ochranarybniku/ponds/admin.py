from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.gis.geos import Point
from ponds.models import Pond


@admin.register(Pond)
class PondAdmin(OSMGeoAdmin):
    list_display = ("pond_name", "monitored")
    list_editable = ("monitored",)
    pnt = Point(15.3,50, srid=4326)
    pnt.transform(900913)
    default_lon, default_lat = pnt.coords
    default_zoom=7
    map_width = 900 
    map_height = 650
    prepopulated_fields = {
        "slug": ("pond_name",),
    }
