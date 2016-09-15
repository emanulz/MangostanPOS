# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers, viewsets
from .models import Client
from .filters import ClientFilter


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('client_name','client_last_name', 'client_id_type', 'client_id', 'client_address', 'client_phone',
                  'client_email', 'client_has_credit', 'client_credit_limit', 'client_debt', 'client_credit_days', )


class ClientViewSet(viewsets.ModelViewSet):

    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    lookup_field = 'id'
    filter_class = ClientFilter
