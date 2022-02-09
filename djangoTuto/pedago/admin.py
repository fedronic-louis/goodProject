from django.contrib import admin
from .models import ComposeDe, Suivie

class AdminComposeDe(admin.ModelAdmin):
    list_display=('id','offre','seance')

class AdminSuivie(admin.ModelAdmin):
    list_display=('id','seance','start_stagiaire','demarrage_stagiaire','fin_stagiaire','termine_stagiaire','valide_stagiaire','valide_formateur')

admin.site.register(ComposeDe,AdminComposeDe)
admin.site.register(Suivie,AdminSuivie)
