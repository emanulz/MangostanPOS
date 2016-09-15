# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Client(models.Model):

    person = 'per'
    juridic = 'jur'
    passport = 'pas'

    ID_TYPE_CHOICES = ((person, 'Cédula Física'),
                     (juridic, 'Cédula Jurídica'),
                     (passport, 'Pasaporte'),
                     )

    client_name = models.CharField(max_length=255, verbose_name='Nombre')
    client_last_name = models.CharField(max_length=255, null=True, blank=True)
    client_id_type = models.CharField(max_length=3, choices=ID_TYPE_CHOICES, default=person, verbose_name='Tipo de Identificación')
    client_id = models.CharField(max_length=255, null=True, blank=True, verbose_name='Num Identificación')
    client_address = models.CharField(max_length=255, null=True, blank=True, verbose_name='Dirección')
    client_phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Teléfono')
    client_email = models.EmailField(null=True, blank=True, verbose_name='Email')
    client_has_credit = models.BooleanField(default=False, verbose_name='Tiene Crédito?')
    client_credit_limit = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Límite de Crédito', null=True, blank=True)
    client_debt = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Saldo', null=True, blank=True)
    client_credit_days = models.PositiveIntegerField(default=30, null=True, blank=True, verbose_name='Días de Crédito')

    def __unicode__(self):
        return '%s %s' % (self.client_name, self.client_last_name)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']



