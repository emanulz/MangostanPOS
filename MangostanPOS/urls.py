"""MangostanPOS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from frontend.views import AppView
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView

from rest_framework import routers
# Clients
from clients.restframework import ClientViewSet
# Products
from products.restframework import ProductViewSet, ProductDepartmentViewSet, ProductSubDepartmentViewSet
# Sales
from sales.restframework import SaleViewSet, SaleDetailViewSet, PayDetailViewSet, PayCreditCardTypeViewSet
from sales.restframework import PayMethodViewSet, PayCurrencyViewSet, CreditPaymentViewSet

router = routers.DefaultRouter()
# Clients
router.register(r'clients', ClientViewSet)
# Products
router.register(r'products', ProductViewSet)
router.register(r'productdepartments', ProductDepartmentViewSet)
router.register(r'productsubdepartments', ProductSubDepartmentViewSet)
# Sales
router.register(r'sales', SaleViewSet)
router.register(r'saledetails', SaleDetailViewSet)
router.register(r'paydetails', PayDetailViewSet)
router.register(r'creditcardtypes', PayCreditCardTypeViewSet)
router.register(r'paymethods', PayMethodViewSet)
router.register(r'paycurrencies', PayCurrencyViewSet)
router.register(r'creditpayments', CreditPaymentViewSet)

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^sales/sale/', TemplateView.as_view(template_name="sales/sale.jade")),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^', TemplateView.as_view(template_name="layout/landing.jade")),

]
