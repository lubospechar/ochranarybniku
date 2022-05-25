from django.shortcuts import render
from cal.models import PondVisit
import datetime

def home(request):
    past_visits = PondVisit.objects.filter(
        dt_end__lte=datetime.datetime.now()
    )
    
    future_visits = PondVisit.objects.filter(
        dt_end__gte=datetime.datetime.now()
    )
    
    return render(request, 'cal/home.html', {
        'visits': (future_visits, past_visits)
    })
    
