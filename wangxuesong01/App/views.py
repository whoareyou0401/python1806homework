from django.shortcuts import render
from django.http import HttpResponse
from App.models import *
# Create your views here.
def hello(request):
    return HttpResponse("Django有点蒙啊")


def helloT(request):
    return render(request,"hellodjango.html")


def my_person(req):
    persons = Person.objects.all()
    return render(req,"my_person.html",context={"per":persons})

def my_company(req):
    coms = Company.objects.all()
    return render(req,"companys.html",context={"companies":coms})