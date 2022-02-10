from django.db import models
import PIL

class Lab(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20, blank=True, default="none")
    sigle = models.CharField(max_length=20, blank=True, default="none")
    intitule = models.CharField(max_length=500, blank=True, default="none")
    grn = models.ForeignKey('administration.Grn', blank=True, null=True, on_delete=models.PROTECT)
    milisime = models.CharField(max_length=20, blank=True, default="none")

    imageDescription = models.CharField(max_length=255,null=True)
    picture = models.ImageField(upload_to='pics/', null=True)#settings.MEDIA_ROOT
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return "%s %s" % (self.sigle, self.code)


class Module(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20, blank=True, default="none")
    description = models.CharField(max_length=200, blank=True, default="none")
    lab_attache = models.ForeignKey('Lab', blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return "%s" % self.description


class Sequence(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20, blank=True, default="none")
    description = models.CharField(max_length=200, blank=True, default="none")
    module_attache = models.ForeignKey('Module', blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return "%s %s %s" % (self.code, self.description, self.module_attache)


class Seance(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20, blank=True, default="none")
    description = models.CharField(max_length=200, blank=True, default="none")
    sequence_attache = models.ForeignKey('Sequence', blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return "%s %s %s" % (self.code, self.description, self.sequence_attache)
