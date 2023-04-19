from django.db import models
from ponds.models import Pond
from webapp.models import Language
from django.utils import translation

def get_lang():
    return Language.objects.get(
        lang = translation.get_language()
    )


class Unit(models.Model):
    shortcut = models.CharField(verbose_name="Zkratka", max_length=10)
    description_cs = models.CharField(verbose_name="Popis", max_length=255)
    #description_en = models.CharField(verbose_name="Popis (en)", max_length=255)

    class Meta:
        verbose_name = "Jednotka"
        verbose_name_plural = "Jednotky"

    def __str__(self):
        return self.shortcut


class Parameter(models.Model):
    name_cs = models.CharField(max_length=50, verbose_name="Název parametru (cs)")
    note_cs = models.CharField(
        max_length=255, verbose_name="Poznámnka (cs)", null=True, blank=True
    )
    
    datatype = models.PositiveSmallIntegerField(
        choices=((1, "Float"), (2, "Integer"), (3, "Boolean"), (4, "Char")),
        verbose_name="Datový typ",
    )
    unit = models.ForeignKey(Unit, verbose_name="Jednotky", on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        verbose_name = "Parametr"
        verbose_name_plural = "Parametry"

    def __str__(self):
        rstr = self.name_cs
        if self.note_cs: rstr = rstr + f' {self.note_cs}'
        if self.unit: rstr = rstr + f' [{self.unit.shortcut}]'
        return rstr


    def get_name(self):
        try:
            return ParameterTranslation.objects.get(
                parameter=self,
                lang=get_lang()
            ).name
        except ParameterTranslation.DoesNotExist:
            return None

class ParameterTranslation(models.Model):
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    note = models.CharField(max_length=255, null=True, blank=True)


class PondMeasurement(models.Model):
    datetime = models.DateTimeField(verbose_name="Datum")
    pond = models.ForeignKey(Pond, verbose_name="Rybník", on_delete=models.CASCADE)
    note_cs = models.TextField(null=True, blank=True, verbose_name="Poznámka (cs)")

    class Meta:
        verbose_name = "Měření na rybníku"
        verbose_name_plural = "Měření na rybnících"

    def __str__(self):
        return f"{self.datetime}, {self.pond.pond_name}"


class Data(models.Model):
    parameter = models.ForeignKey(
        Parameter, verbose_name="Parametr", on_delete=models.CASCADE
    )
    measurement = models.ForeignKey(
        PondMeasurement, verbose_name="Měření", on_delete=models.CASCADE
    )
    note = models.CharField(
        verbose_name="Poznámka", max_length=255, null=True, blank=True
    )

    def unit(self):
        return self.parameter.unit

    class Meta:
        abstract = True


class FloatData(Data):
    value = models.FloatField(verbose_name="Hodnota")

    class Meta:
        verbose_name = "Data (desetinné číslo)"
        verbose_name_plural = "Data (desetinná čísla)"


class IntegerData(Data):
    value = models.IntegerField(verbose_name="Hodnota")

    class Meta:
        verbose_name = "Data (celé číslo)"
        verbose_name_plural = "Data (celá čísla)"


class BooleanData(Data):
    value = models.BooleanField(verbose_name="Hodnota", default=False)

    class Meta:
        verbose_name = "Data (ano/ne)"
        verbose_name_plural = "Data (ano/ne)"


class CharData(Data):
    value = models.CharField(verbose_name="Hodnota", max_length=50)

    class Meta:
        verbose_name = "Data (řetezec)"
        verbose_name_plural = "Data (řetězce)"
        
class FiedlerData(Data):
    value = models.FloatField(verbose_name="Hodnota")

    class Meta:
        verbose_name = "Data ze stanic (desetinné číslo)"
        verbose_name_plural = "Data ze stanic (desetinná čísla)"
        unique_together = ['parameter', 'measurement']
    
