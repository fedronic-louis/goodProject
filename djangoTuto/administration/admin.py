from django.contrib import admin
from .models import Centre, Personne, Grn


class AdminCentre(admin.ModelAdmin):
    list_display = ('id', 'code', 'nom', 'adresse', 'cp', 'commune')


class AdminGrn(admin.ModelAdmin):
    list_display = ('id', 'code', 'description')


class AdminPersonnes(admin.ModelAdmin):
    list_display = ('id', 'user', 'code', 'profile')


admin.site.register(Centre, AdminCentre)
admin.site.register(Grn, AdminGrn)
admin.site.register(Personne, AdminPersonnes)
