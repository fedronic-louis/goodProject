from django.contrib import admin
from .models import Module, Sequence, Seance, Produit


class AdminProduit(admin.ModelAdmin):
    list_display = ('id', 'code', 'sigle', 'intitule', 'grn', 'milisime')


class AdminModule(admin.ModelAdmin):
    list_display = ('id', 'code', 'description', 'produit_attache')


class AdminSequence(admin.ModelAdmin):
    list_display = ('id', 'code', 'description', 'module_attache')


class AdminSeance(admin.ModelAdmin):
    list_display = ('id', 'code', 'description', 'sequence_attache')


admin.site.register(Produit, AdminProduit)
admin.site.register(Module, AdminModule)
admin.site.register(Sequence, AdminSequence)
admin.site.register(Seance, AdminSeance)
