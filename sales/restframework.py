# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers, viewsets
from .models import Sale, SaleDetail, PayDetail, PayCreditCardType, PayMethod, PayCurrency, CreditPayment
from .filters import SaleFilter, SaleDetailFilter, PayDetailFilter, PayCreditCardTypeFilter, PayMethodFilter
from .filters import PayCurrencyFilter, CreditPaymentFilter

class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = ('id', 'sale_date', 'sale_time', 'sale_client', 'sale_type', 'sale_debt', 'sale_pending', 'sale_iv_amount',
                  'sale_detail', 'sale_disc_per', 'sale_disc_amount', 'sale_sub_total', 'sale_total',
                  'sale_pay_detail',)


class SaleViewSet(viewsets.ModelViewSet):

    serializer_class = SaleSerializer
    queryset = Sale.objects.all()
    lookup_field = 'id'
    filter_class = SaleFilter


class SaleDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleDetail
        fields = ('id', 'sale_detail_product_id', 'sale_detail_product_code', 'sale_detail_description',
                  'sale_detail_product_price', 'sale_detail_amount', 'sale_detail_disc_per', 'sale_detail_disc_amount',
                  'sale_detail_iv_per', 'sale_detail_total',)


class SaleDetailViewSet(viewsets.ModelViewSet):

    serializer_class = SaleDetailSerializer
    queryset = SaleDetail.objects.all()
    lookup_field = 'id'
    filter_class = SaleDetailFilter


class PayDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = PayDetail
        fields = ('id', 'pay_detail_type', 'pay_detail_currency', 'pay_detail_cash', 'pay_detail_change', 'pay_detail_credit',
                  'pay_detail_credit_card', 'pay_detail_credit_card_type', 'pay_detail_credit_card_auth',
                  'pay_detail_check', 'pay_detail_check_num', 'pay_detail_transfer', 'pay_detail_transfer_num', )


class PayDetailViewSet(viewsets.ModelViewSet):

    serializer_class = PayDetailSerializer
    queryset = PayDetail.objects.all()
    lookup_field = 'id'
    filter_class = PayDetailFilter


class PayCreditCardTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PayCreditCardType
        fields = ('id', 'card_type_name', )


class PayCreditCardTypeViewSet(viewsets.ModelViewSet):

    serializer_class = PayCreditCardTypeSerializer
    queryset = PayCreditCardType.objects.all()
    lookup_field = 'id'
    filter_class = PayCreditCardTypeFilter


class PayMethodSerializer(serializers.ModelSerializer):

    class Meta:
        model = PayMethod
        fields = ('id', 'pay_method_name', )


class PayMethodViewSet(viewsets.ModelViewSet):

    serializer_class = PayMethodSerializer
    queryset = PayMethod.objects.all()
    lookup_field = 'id'
    filter_class = PayMethodFilter


class PayCurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = PayCurrency
        fields = ('id', 'pay_currency_name', 'pay_currency_sign', )


class PayCurrencyViewSet(viewsets.ModelViewSet):

    serializer_class = PayCurrencySerializer
    queryset = PayCurrency.objects.all()
    lookup_field = 'id'
    filter_class = PayCurrencyFilter


class CreditPaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CreditPayment
        fields = ('id', 'credit_payment_client', 'credit_payment_date', 'credit_payment_time', 'credit_payment_sales',
                  'credit_payment_detail', 'credit_payment_amount', )


class CreditPaymentViewSet(viewsets.ModelViewSet):

    serializer_class = CreditPaymentSerializer
    queryset = CreditPayment.objects.all()
    lookup_field = 'id'
    filter_class = CreditPaymentFilter