# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Product (models.Model):

    Unit = 'uni'
    Bulk = 'bul'
    Kit = 'kit'

    SELLS_CHOICES = ((Unit, 'Por Unidad'),
                     (Bulk, 'A Granel'),
                     (Kit, 'En Paquete(kit)'),
                     )

    product_description = models.CharField(max_length=255, verbose_name='Descripción del producto', default=' ')
    product_code = models.PositiveIntegerField(verbose_name='Código', unique=True, default=0)
    product_barcode = models.PositiveIntegerField(verbose_name='Código de Barras', blank=True, default=0)
    product_department = models.ForeignKey('ProductDepartment', null=True, verbose_name='Familia', default='')
    product_subdepartment = models.ForeignKey('ProductSubDepartment', null=True, verbose_name='Sub-Familia', default='')
    product_useinventory = models.BooleanField(default=False, verbose_name='Sistema de Inventarios?')
    product_inventory = models.FloatField(default=0, verbose_name='Existencia en Inventario')
    product_minimum = models.FloatField(default=0, verbose_name='Mínimo en inventario')
    product_sellmethod = models.CharField(max_length=3, choices=SELLS_CHOICES, default=Unit,
                                          verbose_name='Se Vende Por')
    product_cost = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Costo ₡')
    product_autoprice = models.BooleanField(default=False, verbose_name='Precio Automático?')
    product_utility = models.DecimalField(default=0, max_digits=5, decimal_places=2, verbose_name='Utilidad %')
    product_price = models.DecimalField(default=0, max_digits=10, decimal_places=2,
                                        verbose_name='Precio sin Impuestos ₡')
    product_usetaxes = models.BooleanField(default=False, verbose_name='Usa Impuestos?')
    product_taxes = models.DecimalField(default=0, max_digits=4, decimal_places=2, verbose_name='Impuestos %')
    product_discount = models.DecimalField(default=0, max_digits=4, decimal_places=2, verbose_name='Descuento %')
    product_sellprice = models.DecimalField(default=0, max_digits=10, decimal_places=2,
                                            verbose_name='Precio de Venta ₡')

    def __unicode__(self):
        return '%s' % self.product_description

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['product_code']


class ProductDepartment(models.Model):

    product_department_name = models.CharField(max_length=255, verbose_name='Nombre de la Familia', unique=True)
    product_department_code = models.CharField(max_length=2, unique=True, verbose_name='Identificador de Familia')

    def __unicode__(self):
        return '%s' % self.productdepartment_name

    class Meta:
        verbose_name = 'Familia'
        verbose_name_plural = 'Familias'
        ordering = ['id']


class ProductSubDepartment(models.Model):

    product_subdepartment_department = models.ForeignKey('ProductDepartment', verbose_name='Familia')
    product_subdepartment_name = models.CharField(max_length=255, verbose_name='Nombre de la Sub-Familia', unique=True)
    product_subdepartment_code = models.CharField(max_length=2, verbose_name='Identificador de Sub-Familia')

    def __unicode__(self):
        return '%s' % self.productsubdepartment_name

    class Meta:
        verbose_name = 'Sub-Familia'
        verbose_name_plural = 'Sub-Familias'
        ordering = ['id']
