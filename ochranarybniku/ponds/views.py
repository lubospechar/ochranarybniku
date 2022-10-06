from django.shortcuts import render, get_object_or_404
from ponds.models import Pond
from data.models import FiedlerData, Parameter, PondMeasurement

def ponds(request):
    return render(request, 'ponds/ponds.html', {
        'ponds': Pond.objects.filter(monitored=True)
    })

def pond_card(request, slug):
    pond = get_object_or_404(Pond, slug=slug)
    
    # dostupná data z stanic fiedler
    parameters = Parameter.objects.filter(
        pk__in=FiedlerData.objects.filter(
            measurement__in=PondMeasurement.objects.filter(pond=pond)
        ).values_list('parameter', flat=True).distinct()
    ).order_by('name_cs')
    

    
    return render(request, 'ponds/pond_card.html', {
        'pond': pond,
        'galleries': pond.photogalleries.all(),
        'pictures': pond.main_photogallery.all(),
        'visits': pond.pondvisit_set.all().order_by('-dt_end'),
        'parameters': parameters,
        
    })
