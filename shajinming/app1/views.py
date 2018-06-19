from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *

# Create your views here.

def hello(requ):
    return HttpResponse("django好棒呦")


def hellot(request):
    return render(request, "helloDjango.html")

def qg(req,):
    person=Person.objects.all()
    return  render(req,"qiming.html",context={"persons":person})