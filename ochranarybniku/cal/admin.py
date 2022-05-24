from django.contrib import admin
from cal.models import PondVisit

@admin.register(PondVisit)
class PondVisitAdmin(admin.ModelAdmin):
    list_display = ('pond' ,'desc', 'dt_start', 'dt_end')
    list_filter = ('pond', )
    
    # změna list_display a exclude pro superuživatele
    def changelist_view(self, request, extra_content=None):
        if request.user.is_superuser:
            self.list_display = ('pond' ,'desc', 'dt_start', 'dt_end', 'user',)
        return super(PondVisitAdmin, self).changelist_view(request, extra_content)

    # queryset pouze pro přihlášeného uživatele
    def get_queryset(self, request):
        qs = super(PondVisitAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.all()
        return qs.filter(user=request.user)

    # uložení aktuálně přihlášeného uživatele
    def save_form(self, request, form, change):
        obj = super().save_form(request, form, change)
        if not request.user.is_superuser:
            obj.user = request.user
        return obj
    
    # exclude user pro normální uživatele
    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('user')
        return super(PondVisitAdmin, self).get_form(request, obj, **kwargs)
