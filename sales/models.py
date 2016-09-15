# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from clients.models import Client


class Sale(models.Model):

    cash = 1
    credit = 2
    mixt = 3

    SELLS_CHOICES = ((cash, 'Contado'),
                     (credit, 'Crédito'),
                     (mixt, 'Mixto'),
                     )

    sale_date = models.DateField(verbose_name='Fecha')
    sale_time = models.TimeField(verbose_name='Hora')
    sale_client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, verbose_name='Cliente', default=1)
    sale_type = models.DecimalField(max_digits=1, decimal_places=0, default=cash, verbose_name='Tipo de venta')
    sale_debt = models.DecimalField(max_digits=11, decimal_places=2, null=True ,blank=True, verbose_name='Saldo Factura')
    sale_pending = models.BooleanField(default=False, verbose_name='Factura Pendiente?', blank=True)
    sale_iv_amount= models.DecimalField(max_digits=11, decimal_places=2, null=True ,blank=True, verbose_name='IV')
    sale_detail = models.ForeignKey('SaleDetail', on_delete=models.SET_NULL, verbose_name='Detalle de la Venta', blank=True, null=True)
    sale_disc_per = models.DecimalField(max_digits=5, decimal_places=2, null=True ,blank=True, verbose_name='Descuento %')
    sale_disc_amount = models.DecimalField(max_digits=11, decimal_places=2, null=True ,blank=True, verbose_name='Descuento Dinero')
    sale_sub_total = models.DecimalField(max_digits=11, decimal_places=2, null=True ,blank=True, verbose_name='Subtotal')
    sale_total = models.DecimalField(max_digits=11, decimal_places=2, null=True ,blank=True, verbose_name='Total')
    sale_pay_detail = models.ForeignKey('PayDetail',  on_delete=models.SET_NULL, null=True, verbose_name='Detalle de Pago')

    def __unicode__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class SaleDetail(models.Model):

    sale_detail_product_id = models.PositiveIntegerField(verbose_name='Id del Artículo')
    sale_detail_product_code = models.PositiveIntegerField(verbose_name='Código del Artículo')
    sale_detail_description = models.CharField(max_length=255, verbose_name='Descripción del Artículo')
    sale_detail_product_price = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True, verbose_name='Precio Unitario')
    sale_detail_amount = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True, verbose_name='Cantidad')
    sale_detail_disc_per = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Descuento %')
    sale_detail_disc_amount = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True, verbose_name='Descuento Dinero')
    sale_detail_iv_per = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='IV %')
    sale_detail_total = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True, verbose_name='Precio Unitario')


    def __unicode__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Venta'
        ordering = ['id']

class PayDetail(models.Model):


    pay_detail_type = models.ForeignKey('PayMethod', default=1, verbose_name='Tipo de Pago')
    pay_detail_currency = models.ForeignKey('PayCurrency', default=1, verbose_name='Moneda')

    pay_detail_cash = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True, verbose_name='Efectivo')
    pay_detail_change = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True, verbose_name='Vuelto')

    pay_detail_credit = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True, verbose_name='Credito')


    pay_detail_credit_card = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True, verbose_name='Tarjeta')
    pay_detail_credit_card_type = models.ForeignKey('PayCreditCardType', null=True, blank=True, default=1, verbose_name='Tipo de Tarjeta')
    pay_detail_credit_card_auth = models.PositiveIntegerField(null=True, blank=True, verbose_name='Autorización')


    pay_detail_check = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True, verbose_name='Cheque')
    pay_detail_check_num = models.PositiveIntegerField(null=True, blank=True, verbose_name='Numero de Cheque')


    pay_detail_transfer = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True, verbose_name='Transferencia')
    pay_detail_transfer_num = models.PositiveIntegerField(null=True, blank=True, verbose_name='Numero de Transferencia')


    def __unicode__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Detalle de Pago'
        verbose_name_plural = 'Detalles de Pago'
        ordering = ['id']
    #
    # cash = 1
    # credit = 2
    # credit_card = 3
    # check = 4
    # transfer = 5
    # mixt = 6
    #
    # colon = 1
    # dolar = 2


class PayCreditCardType(models.Model):

    card_type_name= models.CharField(max_length=255, verbose_name='Tipo de Tarjeta')

    def __unicode__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Tipo de Tarjeta'
        verbose_name_plural = 'Tipos de Tarjeta'
        ordering = ['id']


class PayMethod(models.Model):

    pay_method_name = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Método de Pago'
        verbose_name_plural = 'Métodos de Pago'
        ordering = ['id']


class PayCurrency(models.Model):

    pay_currency_name = models.CharField(max_length=255, verbose_name='Moneda')
    pay_currency_sign = models.CharField(max_length=255, verbose_name='Símbolo de Moneda')

    def __unicode__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Moneda'
        verbose_name_plural = 'Monedas'
        ordering = ['id']

class CreditPayment(models.Model):

    credit_payment_client = models.ForeignKey(Client, verbose_name='Cliente')
    credit_payment_date = models.DateField(verbose_name='Fecha')
    credit_payment_time = models.TimeField(verbose_name='Hora')
    credit_payment_sales = models.ManyToManyField('Sale', blank=True, verbose_name='Facturas')
    credit_payment_detail = models.ForeignKey('PayDetail', on_delete=models.SET_NULL, null=True, verbose_name='Detalles del Pago')
    credit_payment_amount = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True, verbose_name='Monto del Abono')


# Abonos
#
# detalles pago igual que en venta
