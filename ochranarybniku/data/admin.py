from django.contrib import admin
from data.models import (Unit, PondMeasurement, Parameter, FloatData, IntegerData, BooleanData, CharData)

@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ('name', 'note')

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('shortcut', 'description')


class FloatDataInline(admin.TabularInline):
    model = FloatData

class IntegerDataInline(admin.TabularInline):
    model = IntegerData

class BooleanDataInline(admin.TabularInline):
    model = BooleanData

class CharDataInline(admin.TabularInline):
    model = BooleanData

@admin.register(PondMeasurement)
class PondMeasurementAdmin(admin.ModelAdmin):
    list_display = ('date', 'pond', 'note')
    inlines = [
        FloatDataInline,
        IntegerDataInline,
        BooleanDataInline,
        CharDataInline,
    ]

