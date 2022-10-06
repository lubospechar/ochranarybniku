from django.shortcuts import render
from django.http import JsonResponse
from ponds.models import Pond
from data.models import FiedlerData, Parameter, PondMeasurement

def ph(request):
    
    pond = Pond.objects.get(pk=2)

    data = {
        'data': [1, 2, 3,],
        'labels': ['a','b','c'],
    }
    
    if int(request.GET['option'])==5:
        return JsonResponse(data)
    
    pH = Parameter.objects.get(pk=7)
    
    data_ph = FiedlerData.objects.filter(
        parameter = pH
    )
    
    labels = []
    data = []

    
    for d in data_ph:
        data.append(d.value)
        labels.append(d.measurement.datetime)
        
    return JsonResponse({'data': data, 'labels': labels})




#def ponds(request):
    #return render(request, 'ponds/ponds.html', {
        #'ponds': Pond.objects.filter(monitored=True)
    #})

#def pond_card(request, slug):
    #pond = get_object_or_404(Pond, slug=slug)
    
    ## dostupná data z stanic fiedler
    #parameters =Parameter.objects.filter(
        #pk__in=FiedlerData.objects.filter(
            #measurement__in=PondMeasurement.objects.filter(pond=pond)
        #).values_list('parameter', flat=True).distinct()
    #)
    
    #pH = Parameter.objects.get(pk=7)
    
    #data_ph = FiedlerData.objects.filter(
        #parameter = pH
    #)
