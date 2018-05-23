# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    R = HttpResponse()
    R.write(request.GET.get('name'))    
    return R

# Create your views here.
