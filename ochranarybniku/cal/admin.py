from django.contrib import admin
from cal.models import PondVisit
from django.contrib.auth.models import User

# Vymění metodu __str__ třídy User za get_full_name()
def get_full_name(self):
    return self.get_full_name()


User.add_to_class("__str__", get_full_name)


@admin.register(PondVisit)
class PondVisitAdmin(admin.ModelAdmin):
    list_display = ["desc", "dt_start", "dt_end"]
    list_filter = ["ponds"]
    exclude = []

    # přídání user do list_display pokud je uživatel superuser
    def changelist_view(self, request, extra_content=None):
        if request.user.is_superuser:
            if not 'user' in self.list_display:
                self.list_display.append("user")
        return super(PondVisitAdmin, self).changelist_view(request, extra_content)

    # queryset pouze pro přihlášeného uživatele
    def get_queryset(self, request):
        qs = super(PondVisitAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.all()
        return qs.filter(user=request.user)

    # uložení přihlášeného uživatele jako autora návštěvy
    def save_form(self, request, form, change):
        obj = super().save_form(request, form, change)
        if not request.user.is_superuser:
            obj.user = request.user
        return obj

    # exclude user pro normální uživatele
    def get_form(self, request, obj=None, **kwargs):
        if not request.user.is_superuser:
            self.exclude.append("user")
        return super(PondVisitAdmin, self).get_form(request, obj, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "coworkers":
            kwargs["queryset"] = User.objects.exclude(pk=request.user.pk).exclude(
                is_superuser=True
            )
        return super().formfield_for_manytomany(db_field, request, **kwargs)
