# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Cargo(models.Model):

    #__Cargo_FIELDS__
    descripcion = models.CharField(max_length=255, null=True, blank=True)

    #__Cargo_FIELDS__END

    class Meta:
        verbose_name        = _("Cargo")
        verbose_name_plural = _("Cargo")


class Indicador(models.Model):

    #__Indicador_FIELDS__
    descripcion = models.CharField(max_length=255, null=True, blank=True)

    #__Indicador_FIELDS__END

    class Meta:
        verbose_name        = _("Indicador")
        verbose_name_plural = _("Indicador")


class Directivo(models.Model):

    #__Directivo_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)
    apellido = models.CharField(max_length=255, null=True, blank=True)
    sexo = models.IntegerField(null=True, blank=True)

    #__Directivo_FIELDS__END

    class Meta:
        verbose_name        = _("Directivo")
        verbose_name_plural = _("Directivo")


class Evaluacion(models.Model):

    #__Evaluacion_FIELDS__
    directivo = models.ForeignKey(Directivo, on_delete=models.CASCADE)
    edad = models.IntegerField(null=True, blank=True)
    escolaridad = models.IntegerField(null=True, blank=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    exp_cargo = models.IntegerField(null=True, blank=True)
    creado_por = models.IntegerField(null=True, blank=True)

    #__Evaluacion_FIELDS__END

    class Meta:
        verbose_name        = _("Evaluacion")
        verbose_name_plural = _("Evaluacion")


class Evaluaciondetalle(models.Model):

    #__Evaluaciondetalle_FIELDS__
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE)
    valor = models.IntegerField(null=True, blank=True)

    #__Evaluaciondetalle_FIELDS__END

    class Meta:
        verbose_name        = _("Evaluaciondetalle")
        verbose_name_plural = _("Evaluaciondetalle")



#__MODELS__END
