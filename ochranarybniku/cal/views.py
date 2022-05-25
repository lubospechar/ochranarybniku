from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse

import xlwt

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


def pond_visit_to_xls(request):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Návštevy rybníků')
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.bold = True
    style.font = font

    headline = ('Jméno rybníku', 'Začátek návštevy', 'Konec návštěvy', 'Popis aktivit', 'Pracovník')
    col = 0
    row = 0
    for h in headline:
        ws.write(row, col, h, style=style)
        col += 1

    for visit in PondVisit.objects.all():
        row += 1
        ws.write(row, 0, visit.pond.pond_name)
        ws.write(row, 1, str(visit.dt_start))
        ws.write(row, 2, str(visit.dt_end))
        ws.write(row, 3, visit.desc)
        ws.write(row, 4, visit.user.get_full_name())

    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=navstevy_rybniku.xls'
    wb.save(response)
    return response
    
