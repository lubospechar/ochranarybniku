from django.shortcuts import render
from django.utils import timezone
from cal.models import PondVisit

def home(request):
    past_visits = PondVisit.objects.filter(
        dt_end__lte=timezone.now()
    )
    
    future_visits = PondVisit.objects.filter(
        dt_end__gte=timezone.now()
    )
    
    return render(request, 'cal/home.html', {
        'visits': (future_visits, past_visits)
    })
    
