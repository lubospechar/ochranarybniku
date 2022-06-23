from django.contrib import admin
from data.models import (Unit, PondMeasurement)

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('shortcut', 'description')

@admin.register(PondMeasurement)
class PondMeasurementAdmin(admin.ModelAdmin):
    list_display = ('date', 'pond')
