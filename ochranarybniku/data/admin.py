from django.contrib import admin
from data.models import (
    Unit,
    PondMeasurement,
    Parameter,
    FloatData,
    IntegerData,
    BooleanData,
    CharData,
)


class DataAdmin(admin.ModelAdmin):
    list_display = ("measurement", "parameter", "value")

    def get_form(self, request, obj=None, **kwargs):
        form = super(DataAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields["parameter"].queryset = Parameter.objects.filter(
            datatype=self.parameter_datatype
        )
        return form


class DataInline(admin.TabularInline):
    extra = 0

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(DataInline, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )
        if db_field.name == "parameter":
            field.queryset = Parameter.objects.filter(datatype=self.parameter_datatype)
        return field


class FloatDataInline(DataInline):
    model = FloatData
    parameter_datatype = 1


class IntegerDataInline(DataInline):
    model = IntegerData
    parameter_datatype = 2


class BooleanDataInline(DataInline):
    model = BooleanData
    parameter_datatype = 3


class CharDataInline(DataInline):
    model = CharData
    parameter_datatype = 4


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ("name_cs", "name_en", "datatype", "note_cs", "note_en")


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ("shortcut", "description_cs", "description_en")


@admin.register(PondMeasurement)
class PondMeasurementAdmin(admin.ModelAdmin):
    list_display = ("date", "pond", "note_cs", "note_en")
    inlines = [
        FloatDataInline,
        IntegerDataInline,
        BooleanDataInline,
        CharDataInline,
    ]


@admin.register(FloatData)
class FloatDataAdmin(DataAdmin):
    list_display = ("measurement", "parameter", "value", "unit")
    parameter_datatype = 1


@admin.register(IntegerData)
class IntegerDataAdmin(DataAdmin):
    list_display = ("measurement", "parameter", "value", "unit")
    parameter_datatype = 2


@admin.register(BooleanData)
class BooleanDataAdmin(DataAdmin):
    parameter_datatype = 3


@admin.register(CharData)
class CharDataAdmin(DataAdmin):
    parameter_datatype = 4
