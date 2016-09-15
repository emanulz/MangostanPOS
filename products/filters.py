# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from .models import Product, ProductDepartment, ProductSubDepartment


class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Product
        fields = ('product_code', 'product_barcode', 'product_description', 'product_department',
                  'product_subdepartment', 'product_useinventory', 'product_inventory', 'product_minimum',
                  'product_sellmethod', 'product_cost', 'product_autoprice', 'product_utility' , 'product_price',
                  'product_usetaxes', 'product_taxes', 'product_discount', 'product_sellprice',)


class ProductDepartmentFilter(django_filters.FilterSet):

    class Meta:
        model = ProductDepartment
        fields = ('id', 'product_department_name', 'product_department_code', )


class ProductSubDepartmentFilter(django_filters.FilterSet):

    class Meta:
        model = ProductSubDepartment
        fields = ('id', 'product_subdepartment_department', 'product_subdepartment_name', 'product_subdepartment_code',)