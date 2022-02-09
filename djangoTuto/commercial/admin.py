from django.contrib import admin
from .models import Offre, TypeOffre, Inscription, OffreProduit


class AdminOffre(admin.ModelAdmin):
    list_display = ('id', 'code', 'centre', 'type', 'date_debut', 'date_fin')


class AdminOffreProduit(admin.ModelAdmin):
    list_display = ('id', 'offre', 'produit')


class AdminTypeOffre(admin.ModelAdmin):
    list_display = ('id', 'description')


class AdminInscription(admin.ModelAdmin):
    list_display = ('id', 'username', 'code', 'is_afpa')


admin.site.register(Offre, AdminOffre)
admin.site.register(OffreProduit, AdminOffreProduit)
admin.site.register(TypeOffre, AdminTypeOffre)
admin.site.register(Inscription, AdminInscription)
