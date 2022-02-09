from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

CHOICES_ROLE = (
    (0, 'Candidat'),
    (1, 'Formateur'),
    (2, 'Responsable de Formation'),
    (3, 'Assistante Technique'),
    (4, 'Autre4'),
    (5, 'Autre5'),
    (6, 'Autre6'),
)


class Centre(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20, blank=True, default="none")
    nom = models.CharField(max_length=500, blank=True, default="none")
    adresse = models.CharField(max_length=500, blank=True, default="none")
    cp = models.CharField(max_length=6, blank=True, default="none")
    commune = models.CharField(max_length=200, blank=True, default="none")

    def __str__(self):
        return "%s %s" % (self.code, self.nom)


class Grn(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20, blank=True, default="none")
    description = models.CharField(max_length=500, blank=True, default="none")

    def __str__(self):
        return "%s %s" % (self.code, self.description)


class Personne(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=20, blank=True, default="none")
    profile = models.IntegerField(choices=CHOICES_ROLE, blank=True, null=True, default=0)


    def __str__(self):
        return "%s %s %s%s" % (self.id, self.user, self.code, self.profile)
