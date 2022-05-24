from django.db import models
from django.contrib.gis.db.models import PolygonField

class Pond(models.Model):
    pond_name = models.CharField(
        verbose_name='jméno rybníku', max_length=255,
    )
    
    area = PolygonField(
        verbose_name='poloha rybníku (polyogon)'
    )
    
    
