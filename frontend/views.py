from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/admin/login/')
class AppView(TemplateView):

    template_name = 'frontend/base_site2.html'
