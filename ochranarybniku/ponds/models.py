from django.db import models
from django.contrib.gis.db.models import PolygonField

class Pond(models.Model):
    pond_name = models.CharField(
        verbose_name='jméno rybníku', max_length=255,
    )
    
    area = PolygonField(
        verbose_name='poloha rybníku (polyogon)'
    )
    
    def __str__(self):
        return self.pond_name
    
    class Meta:
        verbose_name='Rybník'
        verbose_name_plural='Rybníky'
        

    
    
