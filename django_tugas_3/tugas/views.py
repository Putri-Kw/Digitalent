from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import tugas
# Create your views here.

def tugas(request):
    context = {
        'username' : 'Pejuang'
    }
    template = loader.get_template('tugas.html')
    return HttpResponse(template.render(context, request))

def tugasdb(request):
    data = tugas.objects.all().values()[1]
    context = {
        'data_tugas': data
    }
    template = loader.get_template('tugas2.html')
    return HttpResponse(template.render(context, request))