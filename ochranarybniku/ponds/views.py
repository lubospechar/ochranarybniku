from django.shortcuts import render, get_object_or_404
from ponds.models import Pond

def ponds(request):
    return render(request, 'ponds/ponds.html', {
        'ponds': Pond.objects.filter(monitored=True)
    })

def pond_card(request, slug):
    pond = get_object_or_404(Pond, slug=slug)
    return render(request, 'ponds/pond_card.html', {
        'pond': pond,
        'galleries': pond.photogalleries.all(),
        'pictures': pond.main_photogallery.all(),
        'visits': pond.pondvisit_set.all().order_by('-dt_end')
    })
