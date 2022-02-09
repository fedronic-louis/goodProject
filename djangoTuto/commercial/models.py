from django.contrib.auth.models import User
from django.db import models


class TypeOffre(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=20, blank=True, default="none")

    def __str__(self):
        return "%s" % self.description


class Offre(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(verbose_name='Code offre', max_length=20, blank=True, default="none")
    centre = models.ForeignKey('administration.Centre', blank=True, null=True, on_delete=models.PROTECT)
    type = models.ForeignKey('TypeOffre', blank=True, null=True, on_delete=models.PROTECT)
    date_debut = models.DateField(max_length=12, blank=True, default="none")
    date_fin = models.DateField(max_length=12, blank=True, default="none")

    def __str__(self):
        return "%s %s %s %s %s" % (self.code, self.centre, self.type, self.date_debut, self.date_fin)


class Inscription(models.Model):
    id = models.AutoField(primary_key=True)
    username = User.objects.filter(is_active=True).values_list('username', flat=True)
    code = models.CharField(verbose_name='Code AFPA / stagiaire', max_length=20, blank=True, default="none")
    is_afpa = models.TextField(max_length=1, blank=False, default="0")

    def __str__(self):
        return "%s %s %s %s" % (self.id, self.username, self.code, self.is_afpa)


class OffreProduit(models.Model):
    id = models.AutoField(primary_key=True)
    produit = models.ForeignKey('produit.Produit', blank=True, null=True, on_delete=models.PROTECT)
    offre = models.ForeignKey('Offre', blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return "%s %s %s" % (self.id, self.produit, self.offre)
