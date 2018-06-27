from django.shortcuts import render
from App.models import *
# Create your views here.

def schoolss(req):
    schs = School.objects.all()
    return render(req,"myschool.html",context={"schools":schs,"title":"学习信息"})
