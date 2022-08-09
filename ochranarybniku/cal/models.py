from django.db import models
from django.contrib.auth.models import User
from ponds.models import Pond


class PondVisit(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Uživatel",
        on_delete=models.CASCADE,
        related_name="pond_visitor",
    )

    ponds = models.ManyToManyField(Pond, verbose_name="Rybníky")

    desc = models.CharField(
        max_length=255,
        verbose_name="Stručný popis práce",
    )
    
    desc_en = models.CharField(
        max_length=255,
        verbose_name="Stručný popis práce (en)",
        null=True, blank=True,
    )

    dt_start = models.DateTimeField(verbose_name="Začátek")

    dt_end = models.DateTimeField(verbose_name="Konec")

    coworkers = models.ManyToManyField(
        User, verbose_name="Spolupracovníci", related_name="pond_visitor_coworkers", blank=True
    )

    class Meta:
        verbose_name = "Návštěva rybníku"
        verbose_name_plural = "Návštěvy rybníků"

    def visitors(self):
        if self.coworkers.all():
            return f"{self.user.get_full_name ()}, " + ", ".join(
                [
                    coworker.get_full_name()
                    for coworker in self.coworkers.all().order_by("username")
                ]
            )
        else:
            return self.user.get_full_name()

    def ponds_str(self):
        return ', '.join([pond.__str__() for pond in self.ponds.all()])
    ponds_str.short_description = "Rybníky"
