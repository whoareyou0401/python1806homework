from django.shortcuts import render
from myapp.models import *
# Create your views here.

def class_view(req):
    classes = Class.objects.all()
    return render(req,"test.html",context={"classes":classes})

def stu_view(req):
    stus = student.objects.all()
    c_id = req.GET.get("c_id")
    stus = stus.filter(class_id=c_id)
    return render(req,"test2.html",context={"stus":stus})

