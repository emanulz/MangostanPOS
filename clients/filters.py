# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import django_filters
from .models import Client


class ClientFilter(django_filters.FilterSet):

    class Meta:
        model = Client
        fields = ('client_name','client_last_name', 'client_id_type', 'client_id', 'client_address', 'client_phone',
                  'client_email', 'client_has_credit', 'client_credit_limit', 'client_debt', 'client_credit_days', )