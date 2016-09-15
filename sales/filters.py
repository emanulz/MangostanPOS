# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from .models import Sale, SaleDetail, PayDetail, PayCreditCardType, PayMethod, PayCurrency, CreditPayment


class SaleFilter(django_filters.FilterSet):
    sale_min_date = django_filters.DateFilter(name='sale_date', lookup_type='gte')
    sale_max_date = django_filters.DateFilter(name='sale_date', lookup_type='lte')

    class Meta:
        model = Sale
        fields = ('id', 'sale_date', 'sale_time', 'sale_client', 'sale_type', 'sale_debt', 'sale_pending', 'sale_iv_amount',
                  'sale_detail', 'sale_disc_per', 'sale_disc_amount', 'sale_sub_total', 'sale_total',
                  'sale_pay_detail',)


class SaleDetailFilter(django_filters.FilterSet):

    class Meta:
        model = SaleDetail
        fields = ('id', 'sale_detail_product_id', 'sale_detail_product_code', 'sale_detail_description',
                  'sale_detail_product_price', 'sale_detail_amount', 'sale_detail_disc_per', 'sale_detail_disc_amount',
                  'sale_detail_iv_per', 'sale_detail_total',)


class PayDetailFilter(django_filters.FilterSet):

    class Meta:
        model = PayDetail
        fields = ('id', 'pay_detail_type', 'pay_detail_currency', 'pay_detail_cash', 'pay_detail_change', 'pay_detail_credit',
                  'pay_detail_credit_card', 'pay_detail_credit_card_type', 'pay_detail_credit_card_auth',
                  'pay_detail_check', 'pay_detail_check_num', 'pay_detail_transfer', 'pay_detail_transfer_num', )


class PayCreditCardTypeFilter(django_filters.FilterSet):

    class Meta:
        model = PayCreditCardType
        fields = ('id', 'card_type_name', )


class PayMethodFilter(django_filters.FilterSet):

    class Meta:
        model = PayMethod
        fields = ('id', 'pay_method_name', )


class PayCurrencyFilter(django_filters.FilterSet):

    class Meta:
        model = PayCurrency
        fields = ('id', 'pay_currency_name', 'pay_currency_sign', )


class CreditPaymentFilter(django_filters.FilterSet):

    class Meta:
        model = CreditPayment
        fields = ('id', 'credit_payment_client', 'credit_payment_date', 'credit_payment_time', 'credit_payment_sales',
                  'credit_payment_detail', 'credit_payment_amount', )