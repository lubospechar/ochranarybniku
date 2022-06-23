from django.db import models
from ponds.models import Pond


class Unit(models.Model):
    shortcut = models.CharField(verbose_name="Zkratka", max_length=10)
    description = models.CharField(verbose_name="Popis", max_length=255)

    class Meta:
        verbose_name = "Jednotka"
        verbose_name_plural = "Jednotky"

    def __str__(self):
        return self.shortcut

class Parameter(models.Model):
    name = models.CharField(max_length=50, verbose_name="Název parametru")
    note = models.CharField(max_length=255, verbose_name="Poznámnka", null=True, blank=True)

    class Meta:
        verbose_name = "Parametr"
        verbose_name_plural = "Parametry"

    def __str__(self):
        return self.name


class PondMeasurement(models.Model):
    date = models.DateField(verbose_name="Datum")
    pond = models.ForeignKey(Pond, verbose_name="Rybník", on_delete=models.CASCADE)
    note = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Měření na rybníku"
        verbose_name_plural = "Měření na rybnících"


class FloatData(models.Model):
    float_data = models.FloatField(verbose_name="Hodnota")
    unit = models.ForeignKey(Unit, verbose_name="Jednotky", on_delete=models.CASCADE)
    measurement = models.ForeignKey(
        PondMeasurement, verbose_name="Měření", on_delete=models.CASCADE
    )
    note = models.CharField(
        verbose_name="Poznánka", max_length=255, null=True, blank=True
    )

    class Meta:
        verbose_name = "Data (desetinné číslo)"
        verbose_name_plural = "Data (desetinná čísla)"


class IntegerData(models.Model):
    integer_data = models.FloatField(verbose_name="Hodnota")
    unit = models.ForeignKey(Unit, verbose_name="Jednotky", on_delete=models.CASCADE)
    measurement = models.ForeignKey(
        PondMeasurement, verbose_name="Měření", on_delete=models.CASCADE
    )
    note = models.CharField(
        verbose_name="Poznánka", max_length=255, null=True, blank=True
    )

    class Meta:
        verbose_name = "Data (celé číslo)"
        verbose_name_plural = "Data (celá čísla)"


class BooleanData(models.Model):
    boolean_data = models.BooleanField(verbose_name="Hodnota", default=False)
    unit = models.ForeignKey(Unit, verbose_name="Jednotky", on_delete=models.CASCADE)
    measurement = models.ForeignKey(
        PondMeasurement, verbose_name="Měření", on_delete=models.CASCADE
    )
    note = models.CharField(
        verbose_name="Poznánka", max_length=255, null=True, blank=True
    )

    class Meta:
        verbose_name = "Data (ano/ne)"
        verbose_name_plural = "Data (ano/ne)"


class CharData(models.Model):
    char_data = models.CharField(verbose_name="Hodnota", max_length=50)
    unit = models.ForeignKey(Unit, verbose_name="Jednotky", on_delete=models.CASCADE)
    measurement = models.ForeignKey(
        PondMeasurement, verbose_name="Měření", on_delete=models.CASCADE
    )
    note = models.CharField(
        verbose_name="Poznánka", max_length=255, null=True, blank=True
    )

    class Meta:
        verbose_name = "Data (řetezec)"
        verbose_name_plural = "Data (řetězce)"
