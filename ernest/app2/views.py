# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from .models import TestUpload
# Create your views here.

#def index(request):
    #return render(request, 'index.html')

def testupload(request):
    test_list = TestUpload.objects.all()
    context = {'test_list': test_list}
    path = request.path
    host = request.get_host()
    #return render(request, 'app2/TestUpload.html', path)
    return render_to_response('app2/TestUpload.html', locals())

def newindex(request):
    return render(request, 'app2/newindex.html')