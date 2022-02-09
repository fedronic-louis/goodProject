from django.db import models

class ComposeDe(models.Model):
    id = models.AutoField(primary_key=True)
    offre = models.ForeignKey('commercial.Offre', blank=True, null=True, on_delete=models.PROTECT)
    seance = models.ForeignKey('produit.Seance', blank=True, null=True, on_delete=models.PROTECT)


class Suivie(models.Model):
    id = models.AutoField(primary_key=True)
    seance = models.ForeignKey('ComposeDe',blank=True, null=True, on_delete=models.PROTECT)
    start_stagiaire = models.DateField('Date début par le stagiaire')
    demarrage_stagiaire = models.BooleanField('Démarrage par le stagiaire', default=False)
    fin_stagiaire = models.DateField('Date Fin')
    termine_stagiaire = models.BooleanField('Terminée par le stagiaire', default=False)
    valide_stagiaire = models.BooleanField('Validée par le stagiaire', default=False)
    valide_formateur = models.BooleanField('Validée par le formateur', default=False)
