from django.shortcuts import render
from django.http import JsonResponse
from django.db.models.functions import Trunc
from django.db.models import Avg

from ponds.models import Pond
from data.models import FiedlerData, Parameter, PondMeasurement
import datetime


#data = FiedlerData.objects.filter(measurement__in=PondMeasurement.objects.filter(pond=Pond.objects.get(pk=2))).annotate(week=Trunc('measurement__datetime', 'week')).values('week').annotate(Avg('value'))

def fiedler(request):
    
    pond = Pond.objects.get(pk=2)
    
    parameter_pk = request.GET.get('parameter')
    start_date = request.GET.get('start_date', None)
    end_date = request.GET.get('end_date', None)
    agg = int(request.GET.get('agg'))

    parameter = Parameter.objects.get(pk=parameter_pk)

    if not end_date:
        end_date = FiedlerData.objects.filter(
            parameter = parameter
        ).order_by(
            '-measurement__datetime'
        )[0].measurement.datetime
    
    if not start_date:
        start_date = end_date - datetime.timedelta(days=3)
    
    
    
    labels = []
    data = []

    if agg == 0:
        
        fiedler_data = FiedlerData.objects.filter(
            parameter = parameter,
            measurement__in = PondMeasurement.objects.filter(
                datetime__gte=start_date,
                datetime__lte=end_date,
            )
        ).order_by('measurement__datetime')
        
        
        for d in fiedler_data:
            data.append(d.value)
            labels.append(d.measurement.datetime.strftime("%d.%m.%Y, %H:%M"))
    else:
        agg_config = {
            1: ['hour', "%d.%m.%Y, %H:%M"],
            2: ['day',  "%d.%m.%Y"],
            3: ['week', "%d.%m.%Y"],
            4: ['month', "%d.%m"],
        }
        
        agg_period = agg_config[agg][0]
        date_format = agg_config[agg][1]
        print(agg_period)
        
        fiedler_data = FiedlerData.objects.filter(
            parameter = parameter,
            measurement__in = PondMeasurement.objects.filter(
                datetime__gte=start_date,
                datetime__lte=end_date,
            )
        ).annotate(
            agg=Trunc('measurement__datetime', agg_period)
        ).values('agg').annotate(Avg('value')).order_by('agg')

        for d in fiedler_data:
            data.append(d['value__avg'])
            labels.append(d['agg'].strftime(date_format))
        
        
    return JsonResponse({'data': data, 'labels': labels, 'title': parameter.__str__()})
