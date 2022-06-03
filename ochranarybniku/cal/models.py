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

    pond = models.ForeignKey(Pond, verbose_name="Rybník", on_delete=models.CASCADE)

    desc = models.CharField(
        max_length=255,
        verbose_name="Stručný popis práce",
    )

    dt_start = models.DateTimeField(verbose_name="Začátek")

    dt_end = models.DateTimeField(verbose_name="Konec")

    coworkers = models.ManyToManyField(
        User, verbose_name="Spolupracovníci", related_name="pond_visitor_coworkers"
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
