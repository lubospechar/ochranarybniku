from django.contrib import admin
from cal.models import PondVisit

@admin.register(PondVisit)
class PondVisitAdmin(admin.ModelAdmin):
    list_display = ('pond' ,'desc', 'dt_start', 'dt_end')
    exclude = ('user', )
    
    def save_form(self, request, form, change):
        obj = super().save_form(request, form, change)
        obj.user = request.user
        return obj
    
