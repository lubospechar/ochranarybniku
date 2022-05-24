from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from ponds.models import Pond

@admin.register(Pond)
class PondAdmin(GISModelAdmin):
    pass
